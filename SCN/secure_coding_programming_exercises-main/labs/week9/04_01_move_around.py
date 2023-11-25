"""
Use the following commands to look around your directory
You may want to do this exercise interactively with an interpreter session

Path.cwd() gets the current working directory, returns a Path object
os.chdir(path)  changes directory	

os.listdir() files and directories, returns a list
Path.glob(“*”)  returns a generator that you can use to iterate over all files and directories. Advantage is you can filter the results easily on the input.
Path.iterdir()

"""

from pathlib import Path

# cwd using Path object
cwd = Path.cwd()    
print(cwd)
 
import os
# it gives me the cwd using os module
path = os.getcwd()
print(path)

# we are using os module to change our cwd to another path
os.chdir("week9")
print(Path.cwd())
 
from pprint import pprint
# list the files and the directories
a=os.listdir(r"D:\Mprograms\SCN\secure_coding_programming_exercises-main\labs\week9")
pprint(a)


# Tried glob functio to see how it returns
#Using glob to iterate over all files and directories
for path in Path('.').glob('*'):
    print(path)

from pathlib import Path

# Using glob to iterate over all files and directories and store them in a list
file_list = [str(path) for path in Path('.').glob('*')]
print(file_list)


# Use iterdir to iterate over all files and directories
for path in Path('.').iterdir():
    print(path)
