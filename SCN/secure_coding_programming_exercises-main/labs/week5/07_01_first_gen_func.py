## Write a generator that will produce a list of even numbers

# use a function


def list_of_even_nums(start, stop):
    """
    input:
        start: int
        stop: int
    returns:
        generator object

    Your function should create a generator object that will
    be the sequence of even numbers from start to stop
    Make sure to use the yield keyword!
    """
# The yield keyword is used in the function to make it a generator. 
# When the function is called, it returns a generator object without even starting execution 
# and when the function yields, it transfers control back to the caller with a yield expression’s value.
    for num in range(start, stop+1):
        if num % 2 == 0:
            yield num
            
# The state of the function is remembered and execution continues from where it left off when next() is called again. 
# This allows the function to produce a series of values over time, 
# rather than computing them all at once and sending them back as a list. T



# use your generator
for i in list_of_even_nums(2, 11):
    print(i)
## should print out 2,4,6,8,10
