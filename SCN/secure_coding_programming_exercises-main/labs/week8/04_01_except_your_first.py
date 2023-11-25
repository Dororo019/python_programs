"""
Write a function that accepts user input with the input() function
Try to convert their input to `int` and catch any exceptions that happen.

what kind of exceptions did you find?

"""
def get_integer_input():
    user_input = input("Please enter an integer: ")
    a = int(user_input)
    return a
try:
    print(get_integer_input())
except Exception as e:
    print(f"An error occurred: {e}")
