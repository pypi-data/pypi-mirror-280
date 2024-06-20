#!/usr/bin/python3

"""This module handles the global configuration used throughout the program.
"""

import logging
import os
import platform
from argparse import Namespace
from sys import stdout

# pyudev is only available on Linux
SUPPORTED_PLATFORMS: list = ["Linux"]


class ClonerConfig:
    """The ClonerConfig class is used to pass the various settings between functions.
    This includes things like logging level, whether to print output in color, etc.
    and prevents having to pass numerous arguments throughout the program.
    """

    def __init__(
        self,
        color_mode: bool = False,
        hash_coverage: int = 0,
        rename: bool = False,
        rename_only: bool = False,
        source_directory: str = "",
        source_size: int = 0,
        subdirectories: list = None,
        success_message: str = "",
        temp_directory: str = "",
        trim_files: bool = False,
        verify_only: bool = False,
        very_verbose: bool = False,
        wipe: bool = False,
    ):
        """The constructor for ClonerConfig.
        Stores the configuration used throughout the usbcloner's execution.

        Parameters:
            clone_location (str): Location of files to be copied.
            color_mode (bool): Print logging messages with terminal colors.
            hash_coverage (int): Percentage of files to perform hash verification of.
            rename (bool): Rename files and folders before cloning.
            rename_only (bool: Only rename files and folders, do not clone or verify.
            temp_directory (str: Temporary location used for files to be copied.
            trim_files (bool: Remove any files or folders that are not in the verification table.
            verify_only (bool: Only verify files and folder, do not clone or rename.
            wipe (bool): Wipe devices prior to cloning.
        """

        self.color_mode = color_mode
        self.hash_coverage = hash_coverage
        self.rename = rename
        self.rename_only = rename_only
        self.source_directory = source_directory
        self.source_size = source_size
        self.subdirectories = subdirectories
        self.success_message = success_message
        self.temp_directory = temp_directory
        self.trim_files = trim_files
        self.verify_only = verify_only
        self.very_verbose = very_verbose
        self.wipe = wipe

        # initialize the subdirectories
        if subdirectories is None:
            self.subdirectories = [""]

        # set the success message
        if self.rename_only:
            self.success_message = "RENAMED"
        elif self.verify_only:
            self.success_message = "VERIFIED"
        else:
            self.success_message = "CLONED"

    def __str__(self) -> str:
        """Prints the values of the current configuration."""
        string = ""
        for key, value in vars(self).items():
            string += f"{key} = {value}\n"

        return string


def set_configuration(args: Namespace) -> ClonerConfig:
    """This function is responsible for setting the various configurations used
    throughout execution. This includes things like logging level,
    whether to print output in color, etc.

    Parameters:
        args (Namespace): User provided commandline arguments.

    Returns:
        Usbcloner configuration object to be used throughout execution.
    """

    # set logging level
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(message)s", level=log_level
    )

    # determine whether to primt in color. Defaults to color-mode if we are printing to a tty.
    if args.color_mode:
        output_color = True
    elif args.no_color:
        output_color = False
    else:
        output_color = stdout.isatty()

    # create universal config object
    cloner_config = ClonerConfig(
        color_mode=output_color,
        hash_coverage=args.hash_coverage,
        rename=args.rename,
        rename_only=args.rename_only,
        source_directory=args.source_dir,
        source_size=0,
        subdirectories=args.dirs.split(","),
        trim_files=args.trim_files,
        verify_only=args.verify_only,
        wipe=args.wipe,
        very_verbose=(args.verbose == 2),
    )

    # verify the user-provided commandline arguments
    if not verify_configuration(cloner_config, args.infile):
        return None

    # output configuration information
    print_configuration_info(cloner_config)

    # return configuration object
    return cloner_config


def verify_configuration(cloner_config: ClonerConfig, infile: str) -> bool:
    """Ensures the user-provided settings are valid

    Parameters:
        cloner_config (ClonerConfig): A configuration object for usbcloner.
        infile (str): The file to read in the verification table from.

    Returns:
        Whether the user-provided configuration is valid.
    """

    # can listen on this OS?
    if not validate_os():
        logging.critical(
            "Unable to listen for USB devices on this operating system. Quitting."
        )
        return False

    # does the source directory exist and is it a directory (if provided)?
    if cloner_config.source_directory and not os.path.isdir(
        cloner_config.source_directory
    ):
        logging.critical("Provided source isn't a directory! Quitting.")
        return False

    # does the verification table file exist (if provided)?
    if infile and not os.path.isfile(infile):
        logging.critical("Provided table file does not exist! Quitting.")
        return False

    return True


def print_configuration_info(cloner_config: ClonerConfig) -> None:
    """Prints logging output about which mode the configuration is in"""

    # output entire configuration object to debug
    if cloner_config.very_verbose:
        logging.debug("Current Configuration: \n%s", cloner_config)

    # output settings to user
    if cloner_config.trim_files:
        logging.info("Operating in trim mode. Any extra files will be deleted.")

    # output if we are only renaming files
    if cloner_config.rename_only:
        logging.info(
            "Operating in rename-only mode. No files will be verified or copied."
        )
    elif cloner_config.verify_only:
        logging.info("Operating in verify-only mode. No files will be copied.")

        # warn user these two options combined will wipe everything
        if cloner_config.wipe:
            logging.info(
                "Wiping drives while operating in verify-only mode. "
                "THIS WILL WIPE ALL DRIVES!"
            )
    else:
        logging.info("Operating in cloning mode.")

        if cloner_config.wipe:
            logging.info("Wiping drives prior to cloning.")

    # output percentage of files that will be verified using a hash
    logging.info("Validating the hash for %i%% of files", cloner_config.hash_coverage)


def validate_os(operating_system: str = "") -> bool:
    """Returns if pyudev can execute on a given platform.

    Parameters:
        operating_system (str): The operating system, as a string, to validate.

    Returns:
        Whether pyudev can execute.
    """
    if operating_system:
        return operating_system in SUPPORTED_PLATFORMS
    return platform.system() in SUPPORTED_PLATFORMS
