"""
Construct a code sample where you force an error to happen.
Then run it in a try-except-finally block. But, do NOT catch your error! (Or re-raise it)
Print something out in the finally block.
Does it print out? Why?

The main purpose of the finally is to ensure that some safety code / exit condition will run no matter what, even 
if an error happens.

The purpose of this exercise is to just practice observing that
"""

# An error is forced to happen. 
# The code is run in a try-except-finally block, but the error is not caught. 
# Something is printed out in the finally block.

try:
    print("This is the try block.")
    x = 1 / 0  # This will raise a ZeroDivisionError
except ValueError:
    print("This is the except block.")
finally:
    print("This is the finally block.")

#  ZeroDivisionError is forced to happen in the try block. 
#  However, the except block only catches ValueError, not ZeroDivisionError. 
# Therefore, the error is not caught (or it’s as if it’s re-raised immediately). 
# The finally block prints out a message.

#After running this code, we get to see that “This is the finally block.” is printed out, 
# even though an error occurred that was not caught. 
# This is because the finally block in a try-except-finally structure is always executed, 
# regardless of whether an error occurs or is caught. 
# The main purpose of the finally block is to ensure that some cleanup code or exit condition will run no matter what, 
# even if an error happens.