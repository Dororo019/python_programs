# write a function accepts as input an infinite amount of tuples
# it returns a list, where each element is the inner multiplication

# example input: (1,2), (2,2), (3,2), (4,5)
# output: [2,4,6,20]
def mul_tables(*tuples):
    res=[]
    for a, b in tuples:
        mul = a*b
        res.append(mul)
    return res

print(mul_tables( (1,2), (2,2), (3,2), (4,5)))