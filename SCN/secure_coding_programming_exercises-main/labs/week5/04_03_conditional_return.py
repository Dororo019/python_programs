# write a function that has more than one return statement


def greater_than_x(n, x):
    """
    input:
       n: int
       x: int
    returns:
       True if n > x
       False otherwise
    """
    if n > x:
      return True
    else:
      return False
### Extra credit
# Is it required to use the else block? Can you write the above code with only the if statement but no else?
result = greater_than_x(10, 5)
print(result)

