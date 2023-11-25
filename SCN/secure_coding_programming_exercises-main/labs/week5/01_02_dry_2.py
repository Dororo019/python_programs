# rewrite your function from the previous exercise (01_01_dry.py)
# this time your function should be able change the divisible by number.

# I should be able to return the list of numbers which is divisible by "n", where
# 'n' can be any number.

## Input: a list of integers, a number 'n'
## output: a new list that only has retains numbers which are divisible by n
def num_divisible_by_n(list, n):
    return [i for i in list if i % n == 0]

# Example usage:
numbers = [2, 1, 3, 5, 1, 2, 3, 12, 3, 45, 1, 2, 3]
n= 3
print(num_divisible_by_n(numbers,n))  