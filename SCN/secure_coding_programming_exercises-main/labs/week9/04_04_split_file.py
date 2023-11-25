"""

1. Open winnie_pooh.txt
2. read in 100 lines at a time
3. after each 100 lines, write those lines to a new file
4. name each file differently (create a system to auto-increment the file names)
5. place all the files in a new folder (that you needed to create earlier)


"""
from pathlib import Path

# Create a new directory
new_dir = Path('new_split_files')
new_dir.mkdir(exist_ok=True)
# Open the file
with open('winnie_pooh.txt', 'r') as file:
    lines = file.readlines()

# Split the lines into chunks of 100 lines each
chunks = []
for i in range(0, len(lines), 100):
    chunk = lines[i:i + 100]
    chunks.append(chunk)

# Write each chunk to a new file
for i, chunk in enumerate(chunks):
    with open(new_dir / f'file_{i}.txt', 'w') as new_file:
        new_file.writelines(chunk)
