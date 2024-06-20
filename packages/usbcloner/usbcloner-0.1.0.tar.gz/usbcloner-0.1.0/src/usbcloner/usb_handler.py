#!/usr/bin/python3

"""This module handles the USB objects and associated funtions.
"""

# standard imports
import logging
import os
import shutil
from time import perf_counter

# custom imports
import pyudev

from usbcloner import duplication, renaming, verification
from usbcloner.config_handler import ClonerConfig

# Constants
DRIVE_ADD_STRING: str = "add"
DRIVE_REMOVE_STRING: str = "remove"


class TermColors:
    """Class for terminal color codes"""

    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class USB:
    """A USB object that allows for wiping, cloning, renaming, and validating.
    Can be used with a context manager to automatically mount and unmount the USB drives.

    Attributes:
        name (str): The name of the USB device.
        device_path (str): The path to the USB device (NOT where it is mounted).
        mount_point (str): If the USB is mounted, this is the directory it's mounted at.
        mounted (bool): Whether the USB is mounted or not.
    """

    def __init__(self, device_name: str = "", device_path: str = ""):
        """The constructor for the USB class

        Parameters:
            device_name (str): The name of the device.
            device_path (str): The path to the device.
        """
        # set default variables
        self.name = device_name
        self.device_path = device_path
        self.mount_point = ""
        self.mounted = False
        self.empty: bool

    def __enter__(self):
        """When we use a context manager, start by mounting the device"""
        if not self.mounted:
            self.mount()
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        """When we use a context manager, exit by unmounting the device"""
        if self.mounted:
            self.unmount()

    def __str__(self):
        """Prints the name, device path, and mount path of the USB"""
        return f"{self.name} - {self.device_path} {self.mount_point}"

    def clone(
        self, source_directory: str, source_size: int, subdirectories: list = None
    ) -> bool:
        """Clones all subdirectories to the usb device.

        Parameters:
            source_directory (str): Path to the source files.
            source_size (int): Total size of the source files.
            subdirectories (list): Subdirectories to clone within the source path.

        Returns:
            Returns if the files and folders were all cloned successfully.
        """
        # must be mounted to clone
        if not self.mounted:
            logging.critical("Not mounted. Mount the drive before attempting to clone.")
            return False

        # default the directories to the root of the mounted device
        if subdirectories is None:
            subdirectories = ""

        logging.debug(
            'Starting clone loop from %s with "%s" subdirectories to %s',
            source_directory,
            ", ".join(subdirectories),
            self.mount_point,
        )

        # clone all subdirectories to the device
        for directory in subdirectories:
            # Ensure the directories are not an aboslute path
            # otherwise os.path.join will return the directory by itself. Very bad.
            relative_path = directory[1:] if os.path.isabs(directory) else directory

            # build full paths
            full_source_path = os.path.join(source_directory, relative_path)
            full_destination_path = os.path.join(self.mount_point, relative_path)

            # fail the device if cloning any subdirectory fails
            logging.debug("Cloning %s to %s", full_source_path, full_destination_path)
            if not duplication.copy_folder(
                full_source_path, full_destination_path, source_size
            ):
                logging.critical("Failed to clone to %s", self.mount_point)

                # determine if the drive is empty before returning
                file_list = os.listdir(self.mount_point)
                self.empty = len(file_list) == []
                return False

        # drive is no longer empty
        self.empty = False

        logging.debug("Finished cloning %s", self.mount_point)
        return True

    def mount(self, mount_path: str = "") -> str:
        """Mounts the USB device to a given path.

        Parameters:
            mount_path (str): Path to mount to. Defaults to /mnt/<DEVICE_NAME>.
        """
        # verify proper device name
        if self.name == "":
            raise ValueError("Device name cannot be blank")

        # verify device path exists
        if not os.path.exists(self.device_path):
            raise ValueError("Path to the device does not exist!")

        # mount device
        if not self.mounted:
            # mount based on device name if no mount point given
            if not mount_path:
                mount_path = f"/mnt/{self.name}"

            logging.debug("Mounting %s to %s", self.device_path, mount_path)

            # 256 is the Linux error code for failure to make directory
            if os.system(f"mkdir {mount_path}") != 0:
                logging.error("Failed to create directory %s", mount_path)

            # 8192 is the Linux error code for failure to mount
            if os.system(
                f"mount {self.device_path} {mount_path}"
            ) == 0 and os.path.ismount(mount_path):
                logging.debug("Mounted %s Successfully", self.name)
                self.mount_point = mount_path
                self.mounted = True

                # determine if the drive is empty
                file_list = os.listdir(mount_path)
                self.empty = len(file_list) == []
            else:
                logging.critical("Failed to mount to %s", mount_path)
        else:
            logging.warning("%s is already mounted to %s", self.name, self.mount_point)

        # return mount point
        return self.mount_point

    def unmount(self) -> bool:
        """Unmounts the device and removes the directory it was mounted to."""

        if self.mounted:
            logging.debug("Unmounting %s", self.mount_point)

            # 8192 is the Linux error code for failure to unmount
            if os.system(f"umount {self.mount_point}") == 0:
                logging.debug("Unmounted %s Sucessfully", self.name)
                self.mounted = False
            else:
                logging.error("Failed to unmount %s", self.name)
                return False

            # 256 is the Linux error code returned on failure to delete directory
            if os.system(f"rmdir {self.mount_point}") != 0:
                logging.error("Failed to delete directory %s", self.mount_point)

            # remove the mount point from the object
            self.mount_point = ""
        else:
            logging.warning("Cannot unmount, %s is not currently mounted", self.name)

        # returns if usb is not mounted
        return not self.mounted

    def rename(
        self,
        subdirectories: list = None,
    ) -> bool:
        """Renames files and folders on a USB maintaining lexicographical order.

        Parameters:
            subdirectories (list): Only renames children of the list of subdirectories.
        """
        # must be mounted to rename
        if not self.mounted:
            logging.critical(
                "Not mounted. Mount the drive before attempting to rename."
            )
            return False

        # default the directories to the root of the mounted device
        if subdirectories is None:
            subdirectories = ""

        logging.debug(
            "Renaming %s with %s subdirectories",
            self.mount_point,
            ", ".join(subdirectories),
        )

        # loop through renaming all directories
        success = True
        for directory in subdirectories:
            # ensure the directories are not an aboslute path,
            # otherwise os.path.join will return the directory by itself.
            relative_path = directory[1:] if os.path.isabs(directory) else directory

            # build full path by combining device root with subdirectory
            full_path = os.path.join(self.mount_point, relative_path)

            # rename of all files and folders within path
            logging.debug("Renaming %s", full_path)
            if not renaming.rename_directory(full_path):
                # fail the device if any files or folders are unable to be renamed
                success = False

        logging.debug("Finished rename loop on %s", self.mount_point)
        return success

    def verify(
        self,
        verification_table: dict,
        subdirectories: list = None,
        hash_coverage: int = 0,
        trim_files: bool = False,
        verbose: bool = False,
    ) -> bool:
        """Verifies the directories and files on the USB based on a verification table.

        Parameters:
            verification_table (dict): The table to use for verification. This is required.
            subdirectories (list): Directories to verify. Defaults to the root of the drive.
            hash_coverage (int): What percentage of files to verify the has of. Defaults to 0.
            trim_files (bool): Deletefiles found on the drive that are not in the table.
                THIS CAN WIPE A DRIVE.
            verbose (bool): Print out information for successful verification of files.
        """
        # must be mounted to verify
        if not self.mounted:
            logging.critical(
                "Not mounted. Mount the drive before attempting to verify its contents."
            )
            return False

        # default the directories to the root of the drive
        if subdirectories is None:
            subdirectories = ""

        # verify the directories on the drive
        logging.debug(
            "Verifying %s with the following subdirectories: %s",
            self.mount_point,
            ", ".join(subdirectories),
        )

        # fail the device if any subdirectory fails
        return all(
            verification.verify_directory(
                self.mount_point,
                directory,
                verification_table,
                hash_coverage,
                trim_files,
                verbose,
            )
            for directory in subdirectories
        )

    def wipe(self, verbose: bool = False) -> bool:
        """Deletes all files and folders on the usb drive.

        Returns:
            Returns whether all files and folders were successfully deleted.
        """
        # must be mounted to wipe
        if not self.mounted:
            logging.critical("Not mounted. Mount the drive before attempting to wipe.")
            return False

        # loop through files and folders on device
        logging.debug("Wiping %s", self.mount_point)
        success = True
        for filename in os.listdir(self.mount_point):
            file_path = os.path.join(self.mount_point, filename)

            # try to remove the object
            if verbose:
                logging.debug("Deleting %s", file_path)

            # delete object
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

        logging.debug("Finished wiping %s", self.mount_point)
        self.empty = success
        return success


def operate_on_usb(
    usb: USB, cloner_config: ClonerConfig, verification_table: dict
) -> bool:
    """Conducts the operations on the usb.

    Parameters:
        usb (USB): The USB object to operate on.
        cloner_config (ClonerConfig): The configurations which dictate what to do to the usb.
        verification_table (dict): The table to use to verify the usb.

    Returns:
        Returns whether the operations were all successful or not.
    """
    # wipe the drive first
    if cloner_config.wipe and not usb.wipe(cloner_config.very_verbose):
        logging.critical("Failed to wipe %s!", usb.mount_point)
        return False

    # rename the drive and return in rename-only mode
    if cloner_config.rename_only:
        return usb.rename(cloner_config.subdirectories)

    # verify the drive and return in verify-only mode
    if cloner_config.verify_only:
        return usb.verify(
            verification_table,
            cloner_config.subdirectories,
            cloner_config.hash_coverage,
            cloner_config.trim_files,
            cloner_config.very_verbose,
        )

    # only start cloning if we have enough disk space
    logging.debug("Verifying disk space of %s", usb.mount_point)
    if not duplication.verify_diskspace(cloner_config.source_size, usb.mount_point):
        logging.critical("Not enough diskspace on %s!", usb.mount_point)
        return False

    # clone the usb
    if usb.clone(
        cloner_config.source_directory,
        cloner_config.source_size,
        cloner_config.subdirectories,
    ):
        # verify the files after cloning
        return usb.verify(
            verification_table,
            cloner_config.subdirectories,
            cloner_config.hash_coverage,
            cloner_config.trim_files,
            cloner_config.very_verbose,
        )

    return False


def prompt_for_usb() -> USB:
    """Waits for a device to be plugged in, mounts it, and returns the mounted USB object.

    Returns:
        Returns a USB object of the newly mounted drive.
    """

    # initialize variables
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)

    # only listen for 'block' devices that are partitions
    monitor.filter_by(subsystem="block", device_type="partition")

    # wait for a drive to be plugged in
    print("\n**** Please plug in a source device or press Ctrl+C to quit. ****")
    for device in iter(monitor.poll, None):
        # determine if the drive action was 'added'
        if device.action == DRIVE_ADD_STRING:
            logging.info(
                "Detected USB: %s - %s",
                device.get("ID_FS_LABEL"),
                device.device_node,
            )
            detected_usb = USB(device.sys_name, device.device_node)
            break

    # mount new usb
    detected_usb.mount()

    # return mounted usb
    return detected_usb


def prepare_usb(
    device_name: str,
    device_path: str,
    cloner_config: ClonerConfig,
    verification_table: dict,
) -> bool:
    """Handles the mounting, cloning, renaming, validating, and unmounting of a drive.

    Parameters:
        device_name (str): Name of the device provided by the system.
        device_path (str): Path to the device.
        cloner_config (ClonerConfig): various configurations.
        verification_table (dict): Table to use for verification

    Returns:
        Returns whether we successfully conducted the operation on the drive.
    """

    # start timer
    start_time = perf_counter()

    # perform operations on usb
    with USB(device_name, device_path) as usb:
        if usb.empty:
            logging.critical("%s is empty!", usb.name)
            success = False
        else:
            try:
                success = operate_on_usb(usb, cloner_config, verification_table)
            except KeyboardInterrupt as error:
                logging.critical("Aborting! %s", error)
                success = False

    # calculate execution time
    stop_time = perf_counter()
    time_duration = stop_time - start_time

    # print result
    print_result(
        success,
        cloner_config.success_message,
        device_path,
        time_duration,
        cloner_config.color_mode,
    )

    # return whether we succeeded on this device
    return success


def print_result(
    success: bool,
    success_message: str,
    device_path: str,
    time_duration: float,
    color_mode: bool = False,
):
    """Prints the result of the device operation in a color friendly manner."""
    # add colors if in color-mode
    success_color = TermColors.OKGREEN if color_mode else ""
    fail_color = TermColors.FAIL if color_mode else ""
    end_color = TermColors.ENDC if color_mode else ""

    # print whether we succeeded or not
    if success:
        logging.info(
            "%s%s%s - %s - %0.2f second(s)",
            success_color,
            success_message,
            end_color,
            device_path,
            time_duration,
        )
    else:
        logging.error(
            "%sFAILED%s - %s - %0.2f second(s)",
            fail_color,
            end_color,
            device_path,
            time_duration,
        )
