# Type casting Exercise - 2
# Addition of string and integer using explicit conversion

# Initialise a string variable and integer variable
import sched


a = 10
b = "10"

# After explicit conversion, use python to successfully perform
# the addition of these variables - print the result to the console
sum = f"sum: {a + int(b)}"
print(sum)
## Now try to convert this variable
c = "ten"
print(f'final{sum + c}')


## What kind of error does python give? unsupported operand and value error
## What do you think the reason is? sum has int value and c has a str value so it cannot add two different operands together 
