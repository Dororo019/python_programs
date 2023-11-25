### This code creates a random list for you to use
import random

list_length = random.randint(1, 20)
randlist = list()
for i in range(list_length):
    randlist.append(random.randint(1, 100))


# Write a script that takes randlist (a list of numbers) and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
print(randlist)
num_list=(sorted(randlist))
print("Sorted list:",num_list)

# Looking for repeated strings in num_list and add 0 to the odd item
for items in  num_list :
    if num_list.count(items) ==1:
       num_list.append('0')
    else:
        num_list.append('1')
    continue
print(num_list)




    # print("how:",num_list.count())
    # if res.count(i)==1:
        # res=(items,0)
        
    # else:
        # res =(items,items+1)

# print(res)
# Note: This lab might be challenging! Make sure to discuss ask questions
# and get help!  You will need a python function called `sort`

# example input :[1,2,5,1,2]
# example output :[(1,1), (2,2), (5,0)]
