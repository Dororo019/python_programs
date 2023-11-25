"""
Wrap the code below so the exception will be caught.

Handle the exception by adding the desired key with a default value.


"""

my_dict = {1: 2, 3: 4}
# print(my_dict["hi"])

try:
    print(my_dict["hi"])
except KeyError:
    my_dict["hi"] = "default"
    print(my_dict["hi"])

# The correct exception to use here is KeyError, 
# which occurs when you try to access a key that does not exist in the dictionary. 
# When the exception is hit, we add the desired key with a default value.

# In this code, if “hi” is not a key in my_dict, 
# it will add “hi” with a default value of “default” and 
# then print the value of “hi”.
# This effectively handles the KeyError by adding the desired key with a default value.