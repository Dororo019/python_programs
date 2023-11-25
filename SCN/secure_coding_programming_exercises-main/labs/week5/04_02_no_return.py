# write a function that does not return any variable!


def print_your_name_UPPER(name):
    """
    input: str (a name)
    output: None # no return!

    This function Prints out the users name in all uppercase
    """
    print(name.upper())


# What happens when you run your function and attempt to return a variable?
a = print_your_name_UPPER("lower case name")
# what is a? None
