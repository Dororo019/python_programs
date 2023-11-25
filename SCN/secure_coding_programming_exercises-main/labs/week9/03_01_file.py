"""
use a context manager to open the file winnie_pooh.txt

try it two ways
a) make a Path object that points to winnie_pooh.txt
b) just write it in as a string (don't use a Path object)

Both are valid! The first method is the OO way and will yield better programs down the line.
The second way is fine for quick scripts though

## Tasks to try
1. Print out of the first line of the file
2. Print out all the entire file
3. Print in the last line of the file
4. Add a new sentence to the file "I AM A NEW SENTENCE!"
5. 

"""


from pathlib import Path

##


cwd = Path.cwd()
path= Path.cwd().joinpath("week9","winnie_pooh.txt")
print(path)

# 1. Print out the first line of the file
with path.open() as file:
    print(file.readline())

# 2. Print out the entire file
with path.open() as file:
    print(file.read())

# 3. Print the last line of the file
with path.open() as file:
    lines = file.readlines()
    print(lines[-1])

# 4. Add a new sentence to the file
with path.open('a') as file:
    file.write('I AM A NEW SENTENCE!')
