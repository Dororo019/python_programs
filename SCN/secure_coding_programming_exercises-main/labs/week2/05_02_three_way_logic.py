# 1) Initialize variable a to true, b to false and c to true

a = True
b = False
c = True
# 2) If you print(a and b or c) what it will return? Why? it returns true
print(a and b or c)
# Does the order of operations matter? Yes

# 3) Is print(a or b and c) different? nope, but of if you check step by step you will see OR gives TRUE cond except for ForF cond
print(a or b and c)

# 4)Assign c to false and print the value of a and b or c
c = False

print(a and b or c)

# Understand the difference in each scenario
# What is happening here? okie


# 5) Now try to use some ()'s to force python to evaluate it differently.

print(a and b and c)
print(a or b or c)