# USB Cloner

USB Cloner is a Python library for rapidly replicating the contents of a USB.
It also includes various features to wipe drives before cloning, verify the cloning process, and scramble filenames.

## Installation

Use [pip](https://pip.pypa.io/en/stable/) to install usbcloner. Python 3.8 or higher is required.

```bash
pip3 install usbcloner
```

## Usage

### Duplicating USBs

Cloning mode is used to duplicate the contents of one drive to multiple others. Cloning will add files without wiping the drive by default. If there is not enough diskspace, usbcloner will skip the new device and not attempt to clone to it.

```bash
# Begin a cloning session using a user-provided USB. Files will be verified using filesizes only--no hashing.
usbcloner

# Wipe all USBs prior to cloning to ensure there is enough disk space and use hashing to verify file duplication for all files.
usbcloner -w -p 100
```

### Verify USB Contents

Verification mode can be used to ensure the contents of numerous devices are identical without performing any cloning.

```bash
# Prompt for a USB and verify subsequent USB drives.
usbcloner --verify-only

# Build and save a verification table first, then verify devices using the saved table at a later time.
# Without --verify_only, usbcloner will enter into "cloning" mode after saving the verification table.
usbcloner -o "verify.tbl" --verify_only

# At a later time...
usbcloner -i "verify.tbl" --verify_only
```

### Renaming Files

In addition to duplication and verification, usbcloner allows for the scrambling of filenames on a drive. It does this in a way that maintains the lexicographical (alphabetical sort) order of the files and folders.

```bash
# Clone the drives, but scramble the filenames first. All cloned drives will have the same scrambled filenames for the same files.
usbcloner --rename

# Only rename the files that are already on the drive. No cloning or verification.
usbcloner --rename-only
```

### Speed vs Confidence

By default usbcloner only uses filename and file size to verify successful duplication. However, you can use the `-p` flag to use hashing to verify duplication for a user-provided percentage of files (0-100).

```bash
# Do not perform any hash verification for cloned files. This is the default behavior and the same as running "usbcloner".
usbcloner -p 0

# Perform hash verification for 50% of files after cloning.
usbcloner -p 50

# Perform hash verification for all files after cloning.
usbcloner -p 100
```

### Trim

`--trim` removes any files that are found on the drive that are not in the verification table. This is particularly helpful in deleting hidden files that various operating systems add when drives are mounted or viewed. Examples include .DS_Store on OSX and the "System Volume Information" folder on Windows.

```bash
usbcloner --trim
```

### Other Examples

Use a folder on disk to clone instead of a user-provided USB.

```bash
usbcloner -s ~/Folder_to_be_cloned/
```

## Roadmap

* Add pytest tests
* Add a Rich interface that shows cloning progress in realtime.
* Determine if a drive needs to be reformated
* Test the performance of using Rust for the file copy
* Figure out math on better file name length during renames
* Make it so you don't need to use the computer as a temporary file storage

## Ideas

* Figure out how to associate a USB port to a physical port.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.txt)
