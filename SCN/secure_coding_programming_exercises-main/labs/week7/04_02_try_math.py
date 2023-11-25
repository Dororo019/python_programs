""""
import the math library and use it to automatically generate a random list of numbers
You should generate 1000 random numbers.


"""
import random

random_numbers = [random.random() for elem in range(1000)]
print(random_numbers)
