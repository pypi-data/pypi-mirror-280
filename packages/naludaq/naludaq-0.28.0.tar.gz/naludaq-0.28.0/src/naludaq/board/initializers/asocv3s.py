"""Initializer for the aodsv2 eval board

This initializer will run the init sequence for the aodsv2 eval board.
It contains the board-specific startup sequence.
"""
import logging
import time

from naludaq.board.initializers import Initializers
from naludaq.communication import sendI2cCommand
from naludaq.controllers import Si5341Controller, get_dac_controller
from naludaq.helpers.decorators import log_function

logger = logging.getLogger("naludaq.init_asocv3s_eval")


class InitASoCv3S(Initializers):
    def __init__(self, board):
        """Initializer for ASoCv3S.

        Args:
            board (Board): the board to initialize.
        """
        super().__init__(board, "asocv3s")
        self.power_sequence = [
            "2v5_en",
        ]

    def run(self) -> bool:
        """Runs the initialization sequence.

        Returns:
            True, always.
        """
        # Initialize FPGA registers
        self._fpga_init()

        # Power on FMC board
        self._power_toggle(True)
        time.sleep(0.25)

        # Program clock
        self._program_clock()

        # Select parallel interface
        self._set_loopback_enabled(False)
        self._system_reset()
        self._set_com_mode()

        # Chip-side register startup
        self._analog_startup()
        self._digital_startup()

        # External devices
        self._init_dacs()
        self._init_i2c_devices()

        # self.control_registers.write('ser2par_en', True)
        self.control_registers.write("digser_tx_en", True)

        return True

    @log_function(logger)
    def _fpga_init(self):
        """Write all FPGA registers to their default values."""
        self.control_registers.write_all()
        self.i2c_registers.write("i2c_en", True)

    @log_function(logger)
    def _power_toggle(self, state):
        """Toggles the power rails defined in `power_sequence` attribute."""
        for register in self.power_sequence:
            self.control_write(register, state)

    @log_function(logger)
    def _system_reset(self):
        """Toggle the sysrst pin high, then low"""
        self.control_registers.write("sysrst", True)
        self.control_registers.write("sysrst", False)

    @log_function(logger)
    def _set_com_mode(self):
        """Select the serial interface"""
        self.control_registers.write("iomode0", False)
        self.control_registers.write("iomode1", True)

    @log_function(logger)
    def _program_clock(self):
        """Program the clock chip, uses the clockfile in the paramters if it exits."""
        logger.info("Programming clock")
        Si5341Controller(self.board).program(filename=self.board.params["clock_file"])
        time.sleep(0.25)
        self.control_registers.write("clk_noe", False)

    @log_function(logger)
    def _digital_startup(self):
        """Startup the digital side of the chip by programming all registers."""
        self.digital_registers.write_all()

    @log_function(logger)
    def _analog_startup(self):
        """Start the analog side of the chip by programming all registers."""
        self.analog_registers.write_all()
        self._dll_startup()

    @log_function(logger)
    def _dll_startup(self):
        """Starting the delay line on the analog side.

        Sets and unsets vanbuff to get the dll going and
        changes the vadjp values to ensure proper SST duty cycle once locked.
        """
        self.analog_registers.write("qbuff", 0)
        self.analog_registers.write("vanbuff", 0xB00)
        time.sleep(1)
        self.analog_registers.write("qbuff", 2048)
        self.analog_registers.write("vanbuff", 0)

    @log_function(logger)
    def _init_dacs(self):
        """Write the DAC values using the defaults in the YAML."""
        for channel, value in self._get_dac_values().items():
            get_dac_controller(self.board).set_single_dac(channel, value)

    def _get_dac_values(self) -> dict:
        """Return a dict with all the {channels: dac_values}"""
        return self.board.params.get("ext_dac", {}).get("channels", {})

    @log_function(logger)
    def _init_i2c_devices(self):
        """Initialize I2C devices on the eval card"""
        sendI2cCommand(self.board, "30", ["05"])  # tempSensor to temp reg
        sendI2cCommand(self.board, "D0", ["00111011"])  # set up current sense ADC

    @log_function(logger)
    def _set_loopback_enabled(self, enabled: bool):
        """Enable or disable loopback mode."""
        from naludaq.controllers import get_board_controller

        get_board_controller(self.board).set_loopback_enabled(enabled)
