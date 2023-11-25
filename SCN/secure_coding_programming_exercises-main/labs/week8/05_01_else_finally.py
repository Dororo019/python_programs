"""
implement a key-lookup procedure for a dictionary

Try to get the key and update the value by n
If an en exception is raised, handle it by creating the key with a default value
if no exception is raised, update the value
Regardless of what happens, print the dictionary
"""

# A Python function that implements a key-lookup procedure for a dictionary. 
# It tries to get the key and update the value by n. 
# If an exception is raised, it handles it by creating the key with a default value. 
# If no exception is raised, it updates the value. Regardless of what happens, it prints the dictionary.

def update_dict(d, key, n, default):
    try:
        d[key] += n
    except KeyError:
        d[key] = default
    print(d)

# checks the function with a sample dictionary, key, increment value and default value
update_dict({1: 2, 3: 4}, "hi", 1, "default")


# In this code, if “hi” is not a key in the dictionary d, it will add “hi” with a default value of “default”.
# If “hi” is already a key in d, it will increment its value by n. After these operations, it prints the dictionary. 
# This effectively handles the KeyError by adding the desired key with a default value or updating the existing value.