#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""This is a tool to clone or verify a set of directories, files, or drives
    to ensure they were transferred or copied properly.
"""

__version__ = "0.1.0"

# standard imports
import logging
import os
import shutil
import sys
from argparse import ArgumentParser, Namespace
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

# custom imports
import pyudev

from usbcloner import duplication, renaming, usb_handler, verification
from usbcloner.config_handler import ClonerConfig, set_configuration

# Global Variables
# used to tally the total devices detected
global_lock = Lock()
global_total_usbs: int = 0

# used for multithreading
global_thread_pool_exec = ThreadPoolExecutor()

# used in each thread for configurations and for verification
global_config: ClonerConfig
global_verification_table: dict = {}


def prepare_source_folder(cloner_config: ClonerConfig) -> ClonerConfig:
    """Returns the location of files to be cloned.
    Files are copied to a temporary location if they are not already on disk.

    Parameters:
        cloner_config (ClonerConfig): The configuration that will be modified and returned.

    Returns:
        The modified configuration object with the location of files to be cloned.
    """
    # prompt user for a device to clone if there is no source directory provided
    try:
        source_usb = usb_handler.prompt_for_usb()
    except KeyboardInterrupt:
        logging.info("Quitting")
        return None

    # get a source usb from user
    with source_usb:
        # set the size required to clone the files
        cloner_config.source_size = duplication.get_folder_size(source_usb.mount_point)

        # copy files to temporary location
        logging.info("Copying source files to temporary folder")
        cloner_config.source_directory = cloner_config.temp_directory = (
            duplication.copy_to_temp(source_usb.mount_point, cloner_config.source_size)
        )

    # verify source directory is set from a successful copy
    if cloner_config.source_directory:
        logging.info("Cloned files to %s", cloner_config.source_directory)
    else:
        logging.critical("Failed to copy files to temporary directory! Quitting.")
        return None

    # rename the source contents if flag is set
    if cloner_config.rename:
        logging.debug("Renaming temporary files prior to cloning.")
        if renaming.rename_directory(cloner_config.temp_directory):
            logging.debug("Temporary files renamed.")
        else:
            logging.critical("Failed to rename files! Quitting.")
            return None

    # return the configuration object with the clone location set
    return cloner_config


def get_verification_table(cloner_config: ClonerConfig, infile: str = "") -> dict:
    """Get the verification table to be used to verify proper cloning.

    Parameters:
        cloner_config (ClonerConfig): Configurations object storing file locations, verbosity, etc.
        infile (str): User provided verification table file (optional).
    """
    # load or generate a verification table
    verification_table = (
        verification.load_table(infile)
        if infile
        else build_verification_table(cloner_config)
    )

    if not verification_table:
        # we were unable to load or generate a verification table, exit
        logging.critical("Failed to load or create a verification table. Quitting.")
        return None

    # print verification table if very verbose
    if cloner_config.very_verbose:
        verification.print_table(verification_table)

    # returns the modified configurations and verification table
    return verification_table


def build_verification_table(cloner_config: ClonerConfig) -> dict:
    """Make a single verification table based on provided subdirectories.

    Args:
        cloner_config (ClonerConfig): Contains various settings related to cloning behavior.

    Returns:
        The overall table to be used for verification.
    """

    # print debugging information
    logging.debug(
        'Generating combined verification table using %s and "%s" subdirectories',
        cloner_config.source_directory,
        ", ".join(cloner_config.subdirectories),
    )

    # initialize a USB object
    source_usb = usb_handler.USB()

    # if source directory is empty, prompt the user for a usb
    if not (source_dir := cloner_config.source_directory):
        try:
            source_usb = usb_handler.prompt_for_usb()
        except KeyboardInterrupt:
            logging.info("Quitting")
            return None

        source_dir = source_usb.mount_point

    # loop through subdirectories building a combined table
    verification_table = {}
    for subdirectory in cloner_config.subdirectories:
        verification_table.update(
            verification.generate_table(
                source_dir, subdirectory, cloner_config.very_verbose
            )
        )

    # unmount the usb if we used it to generate the verification table
    if source_usb.mounted:
        source_usb.unmount()

    # return generated verification table
    return verification_table


def listen_for_devices() -> None:
    """Start listening for new devices.
    We aren't able to pass ANY arguments to the callback function.

    Returns:
        Once the user presses 'ENTER' this will wait for all threads to complete and exit.
    """

    # initialize pyudev components
    logging.debug("Initializing device monitor")
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)

    # filter at the kernel level to only be notified when a new 'block' subsystem is discovered
    monitor.filter_by(subsystem="block", device_type="partition")

    # set callback function when we are notified by the kernel
    observer = pyudev.MonitorObserver(monitor, callback=device_detected)

    # start monitorying for new devices
    logging.debug("Starting observer")
    observer.start()

    # Listening for devices in the backgroud; this forces the program to block in the foreground.
    # Without this input the program would continue executing.
    input(
        "\n**** Ready to begin. Please plug in new devices. Press ENTER to quit. ****\n"
    )

    # stop the observer from detected new devices
    logging.debug("Stopping observer")
    observer.stop()

    # wait for all threads to exit
    logging.debug("Waiting for threads to exit")
    global_thread_pool_exec.shutdown()

    # delete any temporary files created
    if global_config.temp_directory:
        logging.debug(
            "Removing temporary files located at %s", global_config.temp_directory
        )
        shutil.rmtree(global_config.temp_directory)

    # log number of devices plugged in
    logging.info("Program complete -- Detected %i drives.", global_total_usbs)


def device_detected(device: pyudev.Device) -> None:
    """This is the threaded callback function called by pyudev for each device plugged in.

    Args:
        device (pyudev.Device): The device object passed from pyudev.
    """
    # We must use globals since pyudev doesn't allow variables to be passed to callback functions.
    if device.action == usb_handler.DRIVE_ADD_STRING:
        logging.info("Detected %s - %s", device.device_node, device.get("ID_FS_LABEL"))

        # We don't track threads so we can return and wait for the next device.
        _ = global_thread_pool_exec.submit(
            usb_handler.prepare_usb,
            device.sys_name,
            device.device_node,
            global_config,
            global_verification_table,
        )

        # count the number of devices detected in thread-safe manner
        global global_total_usbs
        with global_lock:
            global_total_usbs += 1

    # log when the user unplugs each drive
    elif device.action == usb_handler.DRIVE_REMOVE_STRING:
        logging.info("Removed %s - %s", device.device_node, device.get("ID_FS_LABEL"))


def usbcloner_main(args: Namespace) -> None:
    """Main function for parsing user-provided arguments and listening for devices.

    Args:
        args (Namespace): User provided commandline arguments.
    """
    # Initialize configurations to be used throughout program execution
    global global_config
    if (global_config := set_configuration(args)) is None:
        logging.critical("Failed to set global configurations! Quitting.")
        sys.exit(1)

    # if only renaming files and folders, skip all verification and cloning prep
    if not global_config.rename_only:
        # in cloning mode, stage the files and set the cloning source path
        if not global_config.verify_only and not global_config.source_directory:
            logging.debug("Preparing files for cloning.")
            if (global_config := prepare_source_folder(global_config)) is None:
                logging.critical("Failed to prepare files for cloning! Quitting.")
                sys.exit(1)

        # stage files and verification table if doing more than renaming
        global global_verification_table
        logging.debug("Getting verification table.")
        if (
            global_verification_table := get_verification_table(
                global_config, args.infile
            )
        ) is None:
            logging.critical("Unable to get a verification table! Quitting.")
            sys.exit(1)

        # store table to disk as a compressed, JSON-encoded dictionary
        if args.outfile:
            logging.debug("Writing verification table to %s", args.outfile)
            verification.save_table(args.outfile, global_verification_table)

    # enter listening mode -- wait for drives to be plugged in then clone / verify them
    logging.debug("Entering listening mode.")
    listen_for_devices()


def main_cli():
    """Entry point for Setuptools."""
    # ensure we are running with root privs so we can mount the drives
    if os.geteuid() != 0:
        logging.critical("You must run this program with root privileges.")
        sys.exit(1)

    # initialize argument parser
    parser = ArgumentParser(
        prog="usbcloner",
        description="A USB duplication and verification tool.",
    )

    # add color parameter group
    color_group = parser.add_mutually_exclusive_group(required=False)
    color_group.add_argument(
        "--color-mode",
        action="store_true",
        default=False,
        help="Color text to indicate successes and failures. "
        "This is the default when outputting to a terminal.",
    )
    color_group.add_argument(
        "--no-color",
        action="store_true",
        default=False,
        help="Suppress colors when outputing text."
        "This is the default when redirecting output to a pipe or file.",
    )

    # parse regular arguments
    parser.add_argument(
        "-d",
        "--subdirectories",
        default="",
        dest="dirs",
        help="Comma delimited list of subdirectories to clone or verify. "
        "Use double-quotes for paths with spaces.",
    )
    parser.add_argument(
        "-s",
        "--source_directory",
        default="",
        dest="source_dir",
        help="The path to clone or build the verification table from.",
    )
    parser.add_argument(
        "-i",
        "--infile",
        default="",
        help="Load verification table from a file.",
    )
    parser.add_argument(
        "-o",
        "--outfile",
        default="",
        help="Save verification table to a file.",
    )
    parser.add_argument(
        "-p",
        "--hash-percent",
        action="store",
        default=0,
        dest="hash_coverage",
        help="Percentage of files to do a hash verification. Range from 0 to 100.",
        # choices=range(0,100),
        # metavar=('0', '-', '100'),
        type=int,
    )
    parser.add_argument(
        "-r",
        "--rename",
        action="store_true",
        default=False,
        help="Rename all the file and folder names maintaining their lexicographic order.",
    )
    parser.add_argument(
        "--rename-only",
        action="store_true",
        default=False,
        dest="rename_only",
        help="Only rename the files and folders on a device. Do not duplicate or verify.",
    )
    parser.add_argument(
        "-t",
        "--trim_files",
        action="store_true",
        default=False,
        help="Delete any extra files that are found on the destination device.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Increase output verbosity. Supports 2 levels of verbosity.",
    )
    parser.add_argument(
        "--verify-only",
        action="store_true",
        default=False,
        dest="verify_only",
        help="Only verify the contents of a drive. Do not copy any contents to it.",
    )
    parser.add_argument(
        "-w",
        "--wipe",
        action="store_true",
        default=False,
        help="Wipe drives before they are cloned.",
    )

    # begin usbcloner with parsed arguments
    usbcloner_main(parser.parse_args())
