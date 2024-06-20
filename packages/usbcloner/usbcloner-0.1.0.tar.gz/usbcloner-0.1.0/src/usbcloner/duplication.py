#!/usr/bin/python3

"""This module performs duplication and preparation functions required for cloning.
"""

# standard imports
import logging
import os
import shutil
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed


def copy_folder(source_folder: str, destination_folder: str, source_size: int) -> str:
    """Copies a folder and all contents to another location. No verification is performed.

    Args:
        source_folder (str): The source of the copy operation.
        destination_folder (str): Where to copy the folder and contents to.
        source_size (int): The size of the source content to be copied.

    Returns:
        Returns if cloning was successful.
    """
    # verify source folder is a directory
    if not os.path.isdir(source_folder):
        logging.debug("Destination is not a folder!")
        return ""

    # ensure there is enough diskspace on the host machine to stage the files
    if verify_diskspace(source_size, tempfile.gettempdir()):
        logging.debug("Verified diskspace")
    else:
        logging.debug("Not enough diskspace!")
        return ""

    # ensure the destination directory exists
    os.makedirs(destination_folder, exist_ok=True)

    # copy files
    logging.debug(
        "Copying %i bytes from %s to %s", source_size, source_folder, destination_folder
    )
    return shutil.copytree(source_folder, destination_folder, dirs_exist_ok=True)


def copy_folder2(
    source_folder: str,
    destination_folder: str,
    source_size: int,
    verbose: bool = False,
) -> str:
    """Copies a folder and all contents to another location. No verification is performed.

    Args:
        source_folder (str): The source of the copy operation.
        destination_folder (str): Where to copy the folder and contents to.
        source_size (int): The size of the content to be copied.
        verbose (bool): Print out file and directory info. Very noisy.

    Returns:
        Returns if cloning was successful.
    """
    # verify source folder is a directory
    if not os.path.isdir(source_folder):
        logging.debug("Destination is not a folder!")
        return ""

    # ensure there is enough diskspace on the host machine to stage the files
    if verify_diskspace(source_size, destination_folder):
        logging.debug("Verified diskspace")
    else:
        logging.debug("Not enough diskspace!")
        return ""

    # ensure the destination directory exists
    os.makedirs(destination_folder, exist_ok=True)

    # loop through directory copying files in a multithreaded manner
    file_futures: list = []
    dir_futures: list = []
    source_folder_len = len(source_folder)

    # with progress.Progress(
    #    progress.TextColumn("[progress.description]{task.description}"),
    #    progress.BarColumn(),
    #    progress.DownloadColumn(),
    #    progress.TransferSpeedColumn(),
    #    progress.TimeElapsedColumn(),
    #    transient=True,
    # ) as progress_bar:

    # add cloning progress bar
    # progress_task = progress_bar.add_task(f"[cyan]Copying {title}", total=source_size)

    # create thread pool to copy files in a threaded manner
    logging.debug(
        "Copying %i bytes from %s to %s",
        source_size,
        source_folder,
        destination_folder,
    )
    with ThreadPoolExecutor() as executor:
        # walk directory and copy all files in threaded manner
        for root, dirs, files in os.walk(source_folder, topdown=True):
            # get the root directory name only
            file_path = root[source_folder_len:]

            if verbose:
                logging.debug("Root Path: %s", root)
                logging.debug("Directories: %s", dirs)
                logging.debug("Files: %s", files)
                logging.debug("File Path: %s", file_path)

            # make all the subdirectories; os.mkdir does not return any value
            for directory in dirs:
                dir_path = os.path.join(destination_folder, file_path, directory)
                if verbose:
                    logging.debug("Creating Directory with mkdir: %s", dir_path)
                dir_futures += executor.map(os.mkdir, dir_path)

            # dir_futures += [
            #    executor.submit(
            #        os.mkdir,
            #        os.path.join(destination_folder, file_path, directory),
            #    )
            #    for directory in dirs
            # ]

            # shutil.copy returns the path of the newly created file or folder
            for file_name in files:
                src_file = os.path.join(root, file_path)
                dst_file = os.path.join(destination_folder, file_path, file_name)
                if verbose:
                    logging.debug("Copying File from %s to %s", src_file, dst_file)
                file_futures.append(executor.map(shutil.copy2, src_file, dst_file))

            # file_futures += [
            #    executor.submit(
            #        shutil.copy2,
            #        os.path.join(root, file_name),
            #        os.path.join(destination_folder, file_path, file_name),
            #    )
            #    for file_name in files
            # ]

            # shutil.copy fails if there isn't a directory, verify the directories were copied
            for dir_future in as_completed(dir_futures):
                directory = dir_future.result()
                if not os.path.isdir(directory):
                    logging.error("Failed to create directory: %s", directory)

        # verify all the files were copied
        for file_future in as_completed(file_futures):
            filename = file_future.result()
            if not os.path.isfile(filename):
                logging.error("Failed to create file: %s", filename)

            # advance the progress bar
            # file_size = os.path.getsize(filename)
            # progress_bar.update(progress_task, advance=file_size)

    # return folder cloned to
    return destination_folder


def copy_to_temp(source_folder: str, source_size: int) -> str:
    """Copies a folder and its contents to a temporary location on disk.

    Args:
        source_folder (str): The source folder to copy to a temporary location.
        source_size (int): The size of the source file.

    Returns:
        Returns the new temporary destination.
    """

    # create temporary folder for storing files to be cloned
    tmp_path = tempfile.mkdtemp()

    # copy the files to the temporary location
    try:
        tmp_path = copy_folder(source_folder, tmp_path, source_size)
    except KeyboardInterrupt:
        logging.critical("Cancelling cloning")

        # clean up the temporary folder
        logging.critical("Deleting temporary directory")
        shutil.rmtree(tmp_path)
        tmp_path = ""

    # verify folder was copied correctly
    if (tmp_folder_size := get_folder_size(tmp_path)) != source_size:
        logging.critical(
            "Failed to copy files correctly! Expected %i but only copied %i. Quitting.",
            source_size,
            tmp_folder_size,
        )
        # clean up the temporary folder
        shutil.rmtree(tmp_path)
        tmp_path = ""

    # return destimation folder
    return tmp_path


def get_folder_size(path: str) -> int:
    """Calculates the size of a folder and all contents in bytes.

    Parameters:
        path (str): The path to calculate the size of.

    Returns:
        The total size of the folder and all content in bytes.
    """
    # verify path is a folder on disk
    if not os.path.isdir(path):
        raise ValueError("Path is not a folder on disk!")

    # loop through directories and files within provided path
    total_bytes = 0
    for dirpath, _, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)

            # skip if it is symbolic link
            if not os.path.islink(filepath):
                total_bytes += os.path.getsize(filepath)

    # return total size in bytes
    return total_bytes


def verify_diskspace(source_size: int, destination_dir: str) -> bool:
    """Verifies there is enough diskspace to copy a folder.

    Parameters:
        destination_dir (str): Where the files will be copied to.
        source_size (int): The size of the source that will be copied.

    Returns:
        Whether the destination has enough diskspace to copy to.
    """
    # we only care about the freespace of the destination
    _, _, freespace = shutil.disk_usage(destination_dir)
    return source_size < freespace
