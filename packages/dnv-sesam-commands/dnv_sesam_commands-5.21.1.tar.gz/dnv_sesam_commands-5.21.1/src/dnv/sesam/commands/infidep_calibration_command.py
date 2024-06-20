"""This module contains the CalibrationCommand class."""

from typing import Optional

from .executable_command_base import ExecutableCommandBase


class CalibrationCommand(ExecutableCommandBase):
    """
    The base class for the Sesam core commands.
    """

    def __init__(
        self,
        input_file_name: Optional[str] = None,
        calibration_directory: Optional[str] = None,
        quick_mode: bool = False,
    ):
        super().__init__(working_dir="")
        self.input_file_name = input_file_name
        self.calibration_directory = calibration_directory
        self.quick_mode = quick_mode

    @property
    def type(self) -> str:
        """
        Gets the type of the command.
        """
        return "DNV.Sesam.Commons.SesamCommands.Infidep.CalibrationCommand, DNV.Sesam.Commons.SesamCommands"

    @property
    def input_file_name(self) -> Optional[str]:
        """
        Gets or sets the name of the calibration input file.
        """
        return self.InputFileName

    @input_file_name.setter
    def input_file_name(self, value: Optional[str]):
        self.InputFileName = value

    @property
    def calibration_directory(self) -> Optional[str]:
        """
        Gets or sets the path to the directory containing the calibration code.

        For cloud runs, this should be left as None.
        """
        return self.CalibrationDirectory

    @calibration_directory.setter
    def calibration_directory(self, value: Optional[str]):
        self.CalibrationDirectory = value

    @property
    def quick_mode(self) -> bool:
        """
        Gets or sets a flag indicating whether the calibration should run in quick mode.

        In quick mode, only two calibration cycles are performed. This will produce incorrect
        results, but allows the workflow to be tested quickly.
        """
        return self.QuickMode

    @quick_mode.setter
    def quick_mode(self, value: bool):
        self.QuickMode = value
