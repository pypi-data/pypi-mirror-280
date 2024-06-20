#!/usr/bin/python3

"""This module performs various verification functions against a directory
    using filesize and the mmh3 hash function. It also allows the saving
    and loading of this information to disk for later verification tasks.
"""

# standard imports
import json
import logging
import os
import random
import zlib
from concurrent.futures import ThreadPoolExecutor, as_completed

# custom imports
import mmh3


def get_file_hash(full_file_path: str) -> int:
    """Calculates the MurmurHash3 of a file.

    Args:
        full_file_path (str): Full path to the file being hashed.

    Returns:
        Returns the mmh3 hash result of a string of bytes.
    """

    # if open fails, default to -1
    file_hash = -1

    # open file and calculate hash
    with open(full_file_path, "rb") as file:
        try:
            file_hash = mmh3.hash(file.read(), signed=False)
        except ValueError:
            logging.error("Read Error: %s", full_file_path)

    return file_hash


def get_file_values(root_dir: str, file_name: str, root_length: int):
    """Calculates the file size and hash of a file

    Args:
        root_dir (str): The directory the file is in
        file_name (str): Name of the file
        root_length (int): Length of the directory to calculate
            the relative file name.

    Returns:
        Returns two values; the relative file path and it's size and hash.


    """
    full_file_path = os.path.join(root_dir, file_name)
    relative_file_path = full_file_path[root_length:]

    # get file size
    file_size = os.path.getsize(full_file_path)

    # get mmh3 hash of file
    file_hash = get_file_hash(full_file_path)

    return relative_file_path, (file_size, file_hash)


def verify_file(
    full_file_path: str,
    gold_size: int,
    gold_hash: int,
    hash_coverage: int,
    verbose: bool = False,
) -> bool:
    """Verifies a file by checking the file size and then the mmh3 hash.

    Args:
        full_file_path (str): Full path to the file being verified.
        gold_size (int): Size the file should be.
        gold_hash (int): Hash the file should have.
        hash_coverage (int): Percent of files that should be verified using the hash.
        verbose (bool): Output information for each file when it succeeds or fails.

    Returns:
        Returns a boolean whether the file was verified or not.
    """

    # Verify the file's size--move to next iteration to save time on failure.
    if (file_size := os.path.getsize(full_file_path)) == gold_size:
        if verbose:
            logging.debug("PASSED - Size Test: %s", full_file_path)
    else:
        logging.warning(
            "FAILED - Size Test: %s: Expected %s bytes but file was %s.",
            full_file_path,
            gold_size,
            file_size,
        )

        # failed size test
        return False

    # generate percentage for hash coverage
    random_coverage = random.randint(1, 100)
    if verbose:
        logging.debug(
            "Hash Verification: %i of %i%%.",
            random_coverage,
            hash_coverage,
        )

    # only perform full verification for a portion of the directories tested
    if random_coverage <= hash_coverage:
        # Verify the file's hash
        if (file_hash := get_file_hash(full_file_path)) == gold_hash:
            if verbose:
                logging.debug("PASSED - Hash Test - %s", full_file_path)
        else:
            logging.warning(
                "FAILED - Hash Test - %s: Expected %s but calculated %s",
                full_file_path,
                gold_hash,
                file_hash,
            )

            # failed hash test
            return False

    # randomly generated number wasn't above the percentage, skip hash check
    elif verbose:
        logging.debug("SKIPPED - Hash Test - %s", full_file_path)

    # passed all tests
    return True


def verify_directory(
    root_directory: str,
    subdirectory: str,
    verification_table: dict,
    hash_coverage: int,
    trim_files: bool,
    verbose: bool = False,
) -> bool:
    """Walks a directory and compares every file there against the verification table.
    First, it checks if the file is in the table.
    Second, it checks if the file is the correct size.
    Finally, it will randomly determine if it should check the MurmurHash3

    After all files have been checked, it will then confirm the number of files found
    match the number of files in the verification table.

    Args:
      root_directory (str): This is the root of where to list files
      subdirectory (str): This is the subdirectory within the root to check
      verification_table (dict): The lookup table that stores the expected size and hash of files.
      hash_coverage (int): What percentage of files to verify the hash of.
      trim_files (bool): Deleted any files that are found and not in the verificaiton table.
      verbose (bool): Output information for each file being verified.

    Returns:
        Returns whether all files in the directory matched or not
    """
    # count to ensure all the files were verified
    num_files_verified = 0
    total_num_files = len(verification_table)

    # standardize the root directory to not have a trailing '/' path delimiter
    if root_directory and root_directory.endswith(os.path.sep):
        root_directory = root_directory[:-1]
    root_length = len(root_directory) + len(os.path.sep)

    # standardize the subdirectory to have a leading '/' path delimiter
    if subdirectory and subdirectory[0] != os.path.sep:
        subdirectory = os.path.join(os.path.sep, subdirectory)

    logging.debug("Root Directory: %s", root_directory)
    logging.debug("Subdirectory: %s", subdirectory)

    # verify all files
    # recursively loops through all files in the path
    with ThreadPoolExecutor() as executor:
        # list of futures threads
        futures = []

        # os.walk returns tuple (root, dirs, files). We don't use dirs.
        for root, _, files in os.walk(root_directory + subdirectory):
            # loop through all files found
            for file_name in files:
                full_file_path = os.path.join(root, file_name)

                # files are stored in the table based on their relative path
                relative_file_path = full_file_path[root_length:]
                if verbose:
                    logging.debug("Looking for %s ", relative_file_path)
                if relative_file_path in verification_table:
                    if verbose:
                        logging.debug("Verifying File: %s", relative_file_path)

                    # pull out expected size and hash for file
                    gold_size, gold_hash = verification_table[relative_file_path]

                    # create thread to verify file
                    futures += [
                        executor.submit(
                            verify_file,
                            full_file_path,
                            gold_size,
                            gold_hash,
                            hash_coverage,
                            verbose,
                        )
                    ]

                # file is not in the verification table
                else:
                    logging.debug("WARNING - Extra File Found: %s", full_file_path)

                    # delete extra files
                    if trim_files:
                        logging.debug("Trim Mode: Removing %s", full_file_path)
                        os.remove(full_file_path)

        # loop through all thread results to see if any files failed
        for future in as_completed(futures):
            if future.result():
                num_files_verified += 1
            else:
                # no need to keep looping if one file failed verification
                break

        # verify the number of files that passed
        if num_files_verified != total_num_files:
            # we did not verify all files
            logging.warning(
                "FAILED - Incorrect number of files on %s: "
                "Found %s of %s files in the verification table",
                root_directory,
                num_files_verified,
                total_num_files,
            )
            verified = False
        else:
            verified = True

    # return success of comparison
    return verified


def generate_table(
    root_directory: str, subdirectory: str, very_verbose: bool = False
) -> dict:
    """Generates a dictionary of key-value pairs consisting of:
    - The filename (without the path) as the key.
    - The value is a tuple with the file size in bytes and the mmh3 hash.

    Args:
        root_directory (str): Path to generate the verification table from.
        subdirectory (str): Subdirectory to add to the root. Consider removing.
        very_verbose (bool): Print the value pair for each file as it's stored.

    Returns:
        Returns dictionary containing a verification table of all file sizes and hashes.
    """

    # initialize lookup table
    verification_table: dict = {}

    # standardize the root directory to have a trailing path delimiter
    if root_directory and not root_directory.endswith(os.path.sep):
        # cannot use os.path.join because the second argument is an absolute path
        root_directory = root_directory + os.path.sep
    root_length = len(root_directory)

    # standardize the subdirectory to not have a leading path delimiter
    if subdirectory and subdirectory[0] == os.path.sep:
        subdirectory = subdirectory[1:]

    # output the normalized path we are using
    full_path = root_directory + subdirectory
    logging.debug("Building verification table for %s", full_path)

    # ensure path exists
    if not os.path.isdir(full_path):
        logging.error("%s does not exist!", full_path)
        return verification_table

    # recursively loop through all files in the path
    # os.walk returns tuple (root, dirs, files). We don't use dirs.
    with ThreadPoolExecutor() as executor:
        futures = []

        logging.debug("Walking path and spawning threads to get verification values")
        for root_dir, _, files in os.walk(full_path):
            futures += [
                executor.submit(get_file_values, root_dir, file_name, root_length)
                for file_name in files
            ]

        # store the gold values generated for each file as they complete
        logging.debug("Storing values in verification table as threads complete")
        for future in as_completed(futures):
            relative_file_path, values = future.result()
            verification_table[relative_file_path] = values
            if very_verbose:
                logging.debug(
                    "Created Entry: %s - %s",
                    relative_file_path,
                    verification_table[relative_file_path],
                )

    # log path used to create golden image
    logging.info("Verification Table Complete: %s", full_path)

    # return lookup table
    return verification_table


def save_table(path: str, verification_table: dict) -> None:
    """Saves the verification table (dictionary) as a compressed json object.

    Args:
      path (str): Path to save the verification table to.
      verification_table (dict): Verification table to be saved to disk.
    """

    with open(path, "wb") as outfile:
        verification_json = json.dumps(verification_table)
        compressed_json = zlib.compress(verification_json.encode())
        outfile.write(compressed_json)

    logging.info('Saved verification table to "%s"', path)


def load_table(path: str) -> dict:
    """Loads a verification table from a file.
    This is done by decompressing and loading it as a json object.

    Args:
      path (str): Path of the file to load the verification table from.

    Returns:
        Returns a verification table of all the files.
    """

    # initialize verification table
    verification_table = {}

    # open provided file and attempt to load table
    with open(path, "rb") as infile:
        verification_json = zlib.decompress(infile.read())
        verification_table = json.loads(verification_json)
        logging.info('Loaded verification table from "%s"', path)

    return verification_table


def print_table(verification_table: dict) -> None:
    """Prints all the files, sizes, and hashes in a verification table.

    Args:
      verification_table (dict): Table containing file information to be printed.
    """
    for key in verification_table.keys():
        # first value is the size, second value is the mmh3 hash
        logging.debug(
            "Verification File: %s, %i bytes, %i",
            key,
            verification_table[key][0],
            verification_table[key][1],
        )
