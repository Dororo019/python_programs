## unpack the following list into 3 variables

my_list = [1, 2, 3, 1, 23, 12, 31, 2, 2, 2, 2, 3, 2, 3, 2, 3, 2, 3, 21, 2, 3, 1]

# the first variable should contain the first element
# the second variable should contain the second element
# the last variable should contain _the rest of the elements_

## hint: use the * unpacking operator.

first_element, second_element, *rest_of_the_elements = my_list

print("First element:", first_element)
print("Second element:", second_element)
print("rest of the elements:", rest_of_the_elements)