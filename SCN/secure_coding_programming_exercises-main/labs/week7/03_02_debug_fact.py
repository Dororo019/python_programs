## DEBUG THIS CODE


def h_fact(n):
    # don't make n==1,instead make it n<=1
    if n <= 1: 
        return 0
    else:
        a = n - 2 * h_fact(n - 1)
        return a
    

print(h_fact(8))

# here the function itself within its definition so i had to fix with the base case of the recursion.
# the base case is if n == 1: return 0.
# which means that when n becomes 1, the function will return 0. 
# But there’s no condition to handle when n becomes 0 or less. 
# If n is less than 1 and the function is called, it will keep subtracting 1 in the recursive call 
# without ever reaching the base case, leading to an infinite recursion. 
# This will eventually result in a RecursionError
# to avoid this. it should add a condition to handle when n is less than or equal to 1.
