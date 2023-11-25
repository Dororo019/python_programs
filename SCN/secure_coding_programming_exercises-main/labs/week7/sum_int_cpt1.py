
# in one line
def sum_integers(*args):
    return sum(arg for arg in args if type(arg) == int)
print(sum_integers(5, 5, 5, 5))  # Output: 20
print(sum_integers(2, 2, 2, 200.2))
print(sum_integers(1,2,3,4,'hi','hi',(1,2,3), 10))
# mine
def sum_ints(*args):
    total = 0
    for arg in args:
        if type(arg) == int:
            total += arg
    return total

print(sum_ints(1, 2, 3, 4, 'hi', 'hi', (1, 2, 3), 10))