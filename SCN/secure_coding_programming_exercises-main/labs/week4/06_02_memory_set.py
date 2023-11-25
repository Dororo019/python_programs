# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.

# Empty set to store the user input1

numbers = set()
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.# Initialize a variable to keep track of the user's points

# Initialize a variable to keep track of the user's points

points = 5

# They win if they manage to create a set that has more than 10 items.

# you will need the `input()` function to collect information from the user

# Use a while loop to continuously collect user input.

while True:
    # Prompt the user to enter a number
    user_input = input("Enter any number: ")

    #Converts the user input to an integer
    try:
        number = int(user_input)
    except ValueError:
        # If the conversion fails, print an error message and continue the loop
        print("Invalid input!!!Please enter a valid integer.")
        continue

    # Checks if the number is already in the set
    if number in numbers:
        # If yes, print a warning message and deduct a point
        print("You have already entered this number!!!!!!You lose a point:(")
        points -= 1
    else:
        # If no, add the number to the set and print a success message
        numbers.add(number)
        print("Good job! You have added a new number to the set.")

    # Check if the user has lost all their points
    if points == 0:
        # If yes, print a game over message and break the loop
        print("Game over. You have lost all your points.")
        break

    # Check if the user has created a set with more than 10 items
    if len(numbers) > 10:
        # If yes, print a congratulations message and break the loop
        print("Congratulations! You have created a set with more than 10 items.")
        break

# Print the final set
print("The final set is:", numbers)

