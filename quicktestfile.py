import os

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

print(list_files_recursively('./data'))
