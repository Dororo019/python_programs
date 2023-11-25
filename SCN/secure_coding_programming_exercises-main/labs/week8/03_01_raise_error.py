"""
Write a function that accepts user input with the input() function
Specify that they must use alphabet characters only.
Then raise an exception if they enter anything that is not able an alphabet character!

Hint: you can use .isalpha() to check if a character is an alpha character.
"""
def get_alpha_input():
    user_input = input("Please enter alphabet characters only: ")
    if not user_input.isalpha():
        raise ValueError("Invalid input. Only alphabet characters are allowed.")
    return user_input


# check above function
try:
    print(get_alpha_input())
except ValueError as e:
    print(e)
