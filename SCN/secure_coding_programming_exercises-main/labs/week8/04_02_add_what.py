"""
Write a function that takes two inputs and attempts to add them together.

Use a try/except block to catch all possible errors

Try adding
int + int
int + str
str + list
tuple + list
dict + dict
dict + str

Are all the exceptions the same?
"""

def try_adding(a, b):
    try:
        result = a + b
        print(f"The result of adding {a} and {b} is: {result}")
    except Exception as e:
        print(f"An error occurred while trying to add {a} and {b}. Error: {e}")

# Test the function with different types of inputs
try_adding(1, 2)  # int + int
try_adding(1, 'a')  # int + str
try_adding('a', [])  # str + list
try_adding((1, 2), [])  # tuple + list
try_adding({'a': 1}, {'b': 2})  # dict + dict
try_adding({'a': 1}, 'b')  # dict + str


# Using a try/except block to catch all possible errors. 
# When an error occurs, it prints out the error message. 
# The exceptions are not all the same - they depend on the types of inputs being added together. 
# For example, adding an integer and a string will raise a TypeError, because these types cannot be added together. 
# Similarly, adding a dictionary and a string will also raise a TypeError. 
# However, adding two dictionaries together will not raise an error; instead, it will merge the two dictionaries into one. 
# If there are duplicate keys in the dictionaries, the values from the second dictionary will overwrite those from the first.