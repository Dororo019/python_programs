"""
CAUTION
Deleting anything with python will permanently delete the file!
You will not be able to recover anything you delete with python!
USE CAUTION!
CAUTION

Use Path.rmdir() and Path.unlink() to delete a folder and file respectively

"""
from pathlib import Path



#create a new directory
new_dir = Path('new_path_dir')
new_dir.mkdir(exist_ok=True)

# Create a new file
new_file = Path('file.txt')
new_file.touch()

# Delete a file
file_to_delete = Path('file.txt')
if file_to_delete.exists():
    file_to_delete.unlink()

# Delete a directory
dir_to_delete = Path('new_path_dir')
if dir_to_delete.exists():
    dir_to_delete.rmdir()
