# Exercise

# Write a program to find the largest number in a list without using built-in functions

# [1,2,1,3,123123,2,1,3,6,3,1,23,6,123,1235,]
# output = 123123

# use a for loop
list = [1,2,1,3,123123,2,1,3,6,3,1,23,6,123,1235,]

for i in list:
    print("The largest number from the given list is :",max(list))
    break