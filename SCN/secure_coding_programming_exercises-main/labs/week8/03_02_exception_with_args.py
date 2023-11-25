"""
rewrite inner_multiple from  Week 8

# write a function accepts as input an infinite amount of tuples
# it returns a list, where each element is the inner multiplication

# example input: (1,2), (2,2), (3,2), (4,5)
# output: [2,4,6,20]


Iterate over the args summing them up. 
Use an if statement ot check if the user passed tuples.
Raise an exception if they passed something else
"""
def inner_multiple(*args):
    # Checks if all arguments are tuples
    if not all(isinstance(arg, tuple) for arg in args):
        raise ValueError("All arguments must be tuples.")
    
    # Then calculate the inner product for each tuple and return as a list
    return [a*b for a, b in args]
# check above function
try:
    print(inner_multiple((1,2), (2,2), (3,2), (4,5)))
except ValueError as e:
    print(e)

