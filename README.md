# README for Batch File Renamer

## Overview

_Rename Files to Numbers_ is a simple Python script designed to rename all files in a selected folder sequentially with a numeric order, starting from `01`, `02`, and so forth. This tool is particularly useful for organising files in a directory where the order of files is important, such as photos from an event, pages of a document, or any collection of files that need to be sequentially ordered.

## Features

- **Easy to Use**: Utilises a graphical interface to select the folder, making it accessible for users of all technical backgrounds.
- **Automatic Numbering**: Renames files automatically with leading zeros based on the total count of files, ensuring a uniform appearance.
- **Non-Destructive**: Preserves file extensions and only changes the file name to a number.

| Before                                       | After                                      |
| -------------------------------------------- | ------------------------------------------ |
| ![Original folder contents](/img/before.png) | ![Renamed folder contents](/img/after.png) |

## Technical Requirements

- Python 3.x
- tkinter (Should be included with Python 3.x)

## Installation

No formal installation is required. Ensure that Python 3.x is installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

## How to Use

### For Technical Users

1. Save the script as `rename_files_to_numbers.py` on your computer.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is saved.
4. Run the script with Python by typing `python rename_files_to_numbers.py` and press Enter.
5. A dialog box will appear. Select the folder whose files you wish to rename.
6. The script will rename the files and print a confirmation message.

### For Non-Techy Users

Don't worry if you're not familiar with programming or using command-line tools. This tool is designed to be easy for anyone to use. Just follow these simple steps:

1. Ensure that you have Python installed on your computer. You can download it here: [official website](https://www.python.org/downloads/).
2. Create a backup of the folder you're planning to use the script on. This is in case you want to undo the changes.
3. Locate the folder named `rename_files_to_numbers.py` on your computer. It might be in your Downloads folder or wherever you saved it.
4. Double-click on the `main.py` file. A window might pop up asking which program to use. Select "Python" from the list and click "OK."
5. A window will open showing your files and folders. Navigate to the folder you want to organise and click "OK" or "Select Folder" (the exact wording may vary).
6. That's it! The script will work its magic, and you'll find your files renamed numerically in the order they were in. There's nothing more you need to do.

## Notes

- The script does not delete or move your files; it only renames them.

Should you encounter any issues or have questions, feel free to reach out for support or consult someone with a technical background for assistance.

# Legal Disclaimer

This software, "Rename Files to Numbers," is provided "as is," without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors, creators, or copyright holders of this software be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.

By using the "Rename Files to Numbers" software, you, the user, agree to use this tool at your own risk. The user assumes full responsibility for any loss of data, damage to files, or any other forms of loss or damage that result from the use of this software. The creators of this tool will not be liable for any unintended consequences of its use, including, but not limited to, errors in file renaming, loss of data, or damage to your system.

It is highly recommended that you back up your data before using this software to rename files. This precaution will allow you to restore your files to their original state should the need arise.

The "Rename Files to Numbers" tool is intended for use by individuals who understand the risks involved and are willing to accept responsibility for the outcomes of its use. Your decision to download and use this software indicates your acceptance of this disclaimer and your acknowledgment that you are using this tool at your own risk.
