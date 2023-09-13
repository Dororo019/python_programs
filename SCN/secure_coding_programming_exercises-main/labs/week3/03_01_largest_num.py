# Exercise

num_one = 10
num_two = 2
num_three = 1010
num_four = 123

# Use if / else statement to find the largest number.
# numbers = [num_one,num_two,num_three,num_four]
if(num_one>=num_two) and (num_one>num_three) and (num_one>=num_four):
    print("Num 1 is largest number")
    
elif(num_two>=num_three) and (num_two>=num_four) and (num_two>=num_one):
    print("Num 2 is largest number")

elif(num_three>=num_four) and (num_three>=num_one) and (num_three>=num_two):
    print("Num 3 is largest number")

else:
    print("Num 4 is largest number")
