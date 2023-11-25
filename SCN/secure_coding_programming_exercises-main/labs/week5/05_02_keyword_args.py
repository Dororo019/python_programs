## Write a function with keyword arguments
## your function can be a mix of positional and keyword arguments
## it must use a default value for the keyword argument.


def rectangle(length,width=10):
    """
    Input:
        length: int
        width: int, defaults to 10

    
    Returns:
        the area of the rectangle
    """
    return length * width
# calls the function with one arg and default value
area = rectangle(5)
print(f"The area of the rectangle is {area} squnits.")
# new area with two arg replacing the default value
area = rectangle(5,2)
print(f"The area of the rectangle is {area} square units.")