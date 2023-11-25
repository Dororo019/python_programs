"""
Wrap the code below in a try - except
What is the correct exception to use?

Fix the error by "padding" the word with blank spaces when the excption is hit.
"""

word = "hellothis"

# for i in range(12):
    # print(word[i])

# The correct exception to use here is IndexError, 
# which occurs when you try to access an index that is outside the bounds of the list (or string, in this case). 
# When the exception is hit, we “pad” the word with blank spaces.
# So here's mine_the fixed one okay!!!
for i in range(10):
    try:
        print(word[i])
    except IndexError:
        print(' ')

# if i is greater than the length of the word,it will print a blank space instead of raising an IndexError. 
# This effectively “pads” the word with blank spaces.