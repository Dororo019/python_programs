"""
Log errors in the following function

"""
import logging
logging.basicConfig(level=logging.ERROR)
# the function add_em_up with error logging added. 
# The logging reports what went wrong when the function is called.
def add_em_up(*args):
    my_sum = 0
    for i,item in enumerate(args):
        try:
            my_sum += item
        except TypeError as e:
            logging.error(f"Error at argument #{i}: {e}")
    return my_sum


## Your logging should be able to report what went wrong with the follow code
print(add_em_up(1, 2, 3, 4))
print(add_em_up(1, 2, 3, "hi"))
print(add_em_up(1, 2, {3, 4}, "hi"))
print(add_em_up([1, 2, 3], [2, 3, 4], {3, 4}, "hi"))

#If a TypeError occurs when trying to add an item to my_sum, 
# it logs an error message that includes the index of the argumen and the error message. 
# This allows you to see exactly which argument caused the error and what the error was. 
# The logging.error function is used to log error messages. When you run this code with the provided inputs, 
# you will see error messages for the arguments that cannot be added to my_sum.

# HINT: We need to have the logging module imported to use logging.error. 
# If you want to see the error messages printed out while running your script, 
# We might need to configure the logging module to print out messages of level ERROR or higher. 
# we can do this by adding logging.basicConfig(level=logging.ERROR) at the beginning of your script.
