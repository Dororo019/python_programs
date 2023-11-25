"""
Let's make a very basic Path object

"""

from pathlib import Path

##
cwd = Path.cwd()

print(cwd)
## create a new path using concatenation
# you can use cwd.joinpath
# or you can use the special / symbol (overloaded for concatenation)

new_path= Path.cwd().joinpath("winnie_pooh.txt")
## examine your new path object
print(new_path)
## print the following parts
a=new_path
print(a)
# .parent
print(a.parent)
# .anchor
print(a.anchor)
# .name
print(a.name)
# .stem
print(a.stem)
# .suffix
print(a.suffix)
# .parent

## check if your path is a directory or file

## .is_file()
print(a.is_file())
## .is_dir()
print(a.is_dir())
## print out your path and look at the type (you may need to print(type(your_path_here)))
## does it accurately reflect your OS? it showing <class 'pathlib.WindowsPath'>
print(type(a))