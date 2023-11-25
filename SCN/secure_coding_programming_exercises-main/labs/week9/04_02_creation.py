"""
Use pathlib.Path objects to 

a) create a new directory
b) create a new file
c) move a file from your current directory into the new directory

use shutil to
d) copy the file back into the original location (while keeping it in the new directory)

"""
from pathlib import Path

import shutil

#create a new directory
new_dir = Path('new_dir')
new_dir.mkdir(exist_ok=True)

# b) Create a new file
new_file = Path('new_file.txt')
new_file.touch()

# c) Move the new file into the new directory
dest = new_dir / new_file.name
new_file.rename(dest)

# d) Copy the file back into the original location using shutil
shutil.copy2(dest, '.')