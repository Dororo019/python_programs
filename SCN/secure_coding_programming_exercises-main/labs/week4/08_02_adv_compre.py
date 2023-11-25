# write code to generate a dictionary where
# each key is:an integer divisible by 3
# each value is: a list containing the even numbers in the range of key

# Take all the numbers divisible by 3 from 1-301
# example output
# {3: [2], 6: [2,4,6], 9:[2,4,6,8].... 300:[2,4,6,...288]}

# empty dictionary to store the numbers
dict = {}

#  a for Loop  with keys from 1 to 301
for key in range(1, 301):
    # Check if the integer is divisible by 3
    if key % 3 == 0:
        # empty list for the value
        value = []
        # each value having the even numbers in the range of key
        for v in range(2, key + 1, 2):
            # Append the even number to the value list
            value.append(v)
        # Assign the value list to the key in the dictionary
        dict[key] = value

# Print the dictionary
print(dict)
