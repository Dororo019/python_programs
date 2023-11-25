"""
write a function that asks for user input with the input() function
Ask them to create a password that is greater than >6 and <12 characters long ( 6< pwd < 12)

Use an assert statement to validate their password choice

"""
def create_password():
    password = input("Please create a password. It should be greater than 6 and less than 12 characters long: ")
    assert 6 < len(password) < 12, "Invalid password length. It should be greater than 6 and less than 12 characters long."
    return password

# check the function
try:
    print(create_password())
except AssertionError as e:
    print(e)
