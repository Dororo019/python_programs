# Write a script that creates a dictionary of keys, `n`
# and values `n * n` for numbers 1 to 10. For example:
# result = {1: 1, 2: 4, 3: 9, ... and so on}

# use a for-loop

# assign a value n to 10
n = 10

# declare dictionary 
nums = {}

# run loop from 1 to n 
for i in range(1, n+1):
	nums[i] = i * i

# print dictionary 
print(nums)