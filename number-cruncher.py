"""
    Endless Sky Number Cruncher
    Primary Author: Devlyn Coulter, 04-DEC-2024
"""

import os #for file paths
import test
from pprint import pprint #allows me to format console output more easily

def list_files_recursively(directory):
    """Recursively lists all files in a directory.

    Args:
        directory: The directory to list files from.

    Returns:
        A list of all file paths found in the directory and its subdirectories.
    """

    file_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
    return file_list

all_stuff = {}
target_files=list_files_recursively('data')
for target in target_files:
    if 'outfits' in target or 'ships' in target:
        all_stuff[target] = test.tokenize_file(target)

