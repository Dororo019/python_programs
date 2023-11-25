"""

Create two new folders
a. vowel
b. consonant
Iterate over your previously created files from 04_04_split_file.py
Open each file and check if the first word begins in a vowel or consonant
If it begins in a vowel, move the file to the vowel folder
Otherwise move the file to the consonant folder

"""
import os
import shutil
from pathlib import Path

new_dir = Path('new_split_files')
# Create two new directories
vowel_dir = Path('vowel')
consonant_dir = Path('consonant')
vowel_dir.mkdir(exist_ok=True)
consonant_dir.mkdir(exist_ok=True)

# Define vowels
vowels = 'aeiou'

# Iterate over the previously created files
for file_name in os.listdir(new_dir):
    with open(f'new_split_files/{file_name}','r') as file:
        # the fngirst line
        first_line = file.readline()
        # Check the first word from the first line aro indakeming skanggipa character from a string ko mesoka
        first_word = first_line.split()[0]

    





""" 
    if file.is_file():
        # Open each file and check if the first word begins with a vowel or consonant
        with open(file, 'r') as f:
            line = f.readline()
            words = line.split()
            # Check if the line is not empty
            if words:
                first_word = words[0]
                # Ensure the file is closed before moving it
                if first_word[0].lower() in vowels:
                    # If it begins with a vowel, move the file to the vowel folder
                    shutil.move(str(file), str(vowel_dir / file.name))
                else:
                    # Otherwise, move the file to the consonant folder
                    shutil.move(str(file), str(consonant_dir / file.name))
 """