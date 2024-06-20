#!/usr/bin/python3

"""This module handles all naming and renaming functions."""

# standard imports
import logging
import os
from concurrent.futures import ThreadPoolExecutor


def generate_filename(index: int, number_of_characters: int) -> str:
    """Generates a random string used to rename files or directories
    while maintaining lexicographical sort order

    Args:
        index (int): Index of the item in the folder. Used to generate the new name.
        number_of_characters (int): Used to pad the generated name to the correct length.
    """
    if number_of_characters < 1 or number_of_characters > 255:
        raise ValueError(
            "number_of_characters must be a positive integer less than 255."
        )

    # convert index to a string
    new_name = str(index)

    # ensure we have enough characters to display the index
    if len(new_name) > number_of_characters:
        raise ValueError("Not enough characters to generate that index.")

    # pad with leading 0's if necessary
    if len(new_name) < number_of_characters:
        # pad string with leading 0's
        for _ in range(len(new_name), number_of_characters):
            new_name = "0" + new_name

    # return the new name
    return new_name


def rename_directory(
    directory: str, preserve_filetype: bool = True, verbose: bool = False
) -> bool:
    """Renames all the files and directories in a given folder.

    Args:
        directory (str): Directory to rename all the contents of.
        preserve_filetype (bool): Ensure the filetype doesn't change upon rename.
        verbose (bool): Print out file and directory info. Very noisy.

    Returns:
        Whether the rename was successful or not.
    """

    # ensure we aren't trying to rename a file or the root directory of the system
    if not directory or not os.path.isdir(directory) or directory == os.path.sep:
        logging.critical("Invalid path provided for renaming: %s", directory)
        return False

    # multithread the renaming of the files and directories
    with ThreadPoolExecutor() as executor:
        # loop through directory from bottom-up
        # so we don't rename directories while they're being parsed
        for root, dirs, files in os.walk(directory, topdown=False):
            # all files and directories are renamed together in lexicographical order
            combined_items = sorted(dirs + files)

            if verbose:
                logging.debug("Root Path: %s", root)
                logging.debug("Directories: %s", dirs)
                logging.debug("Files: %s", files)
                logging.debug("Ordered Items: %s", combined_items)

            # TODO: this can be calculated more accurately
            # total_items = len(combined_items)
            # number_of_characters = X; solve for X... total_items <= len(ASCII_LOWERCASE) ^ X
            # currently hardcoded to 5 characters which can handle < 100,000 items in one folder
            number_of_characters = 5

            # rename all files and folders
            for index, item in enumerate(combined_items):
                # determine if we should maintain the previous extension
                extension = (
                    os.path.splitext(item)[1]
                    if preserve_filetype and item in files
                    else ""
                )

                # generate new file name
                new_item_name = (
                    generate_filename(index, number_of_characters) + extension
                )

                # generate the original and new paths
                new_path = os.path.join(root, new_item_name)
                original_path = os.path.join(root, item)

                # rename the item in a multithreaded manner
                if verbose:
                    logging.debug('Renaming "%s" to "%s"', original_path, new_path)
                _ = executor.submit(os.rename, original_path, new_path)

    return True
