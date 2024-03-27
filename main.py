"""
This script provides functionality to rename all files in a selected folder to numbers.

The script uses tkinter to open a dialog box for the user to select a folder.
All files in the selected folder are then renamed to numbers, maintaining their original order.
The new file names are padded with zeros based on the total number of files,
so that the file names maintain their order when sorted lexicographically.

Functions:
    select_folder: Opens a dialog box for the user to select a folder and returns the selected folder path.
    rename_files_in_folder: Renames all files in the given folder to numbers, maintaining their original order.

Modules:
    os: Provides functions for interacting with the operating system.
    tkinter: Used to create the folder selection dialog box.
"""

import os
from tkinter import Tk
from tkinter import filedialog


def select_folder():
    # Hide the main tkinter window
    Tk().withdraw()

    # Show a dialog box for folder selection and return the selected folder path
    folder_path = filedialog.askdirectory()
    return folder_path


def rename_files_in_folder(folder_path):
    if folder_path:
        # List all files in the directory
        files = os.listdir(folder_path)

        # Filter out directories, leaving only files
        files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

        # Sort files to maintain order
        files.sort()

        # Calculate the number of digits needed for the largest index
        num_files = len(files)
        digits = len(str(num_files))

        # Rename files
        for index, file in enumerate(files, start=1):
            # Define new file name, padded with the calculated number of zeros
            new_file_name = f"{index:0{digits}d}"

            # Extract file extension
            extension = os.path.splitext(file)[1]

            # Construct new file path
            new_file_path = os.path.join(folder_path, f"{new_file_name}{extension}")

            # Construct old file path
            old_file_path = os.path.join(folder_path, file)

            # Rename file
            os.rename(old_file_path, new_file_path)

        print(f"All files in '{folder_path}' have been renamed.")
    else:
        print("No folder was selected. Exiting.")


if __name__ == "__main__":
    folder_path = select_folder()
    rename_files_in_folder(folder_path)
