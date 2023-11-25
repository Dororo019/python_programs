# write a function that takes the length and width of a rectangle and returns the area
def rectangle_area(length, width):
    return length * width

# write another function that finds the area of a cube
def cube_area(a):
    return 6 * (a** 2)

# bonus challenge: use your first function inside this function!
def cube_area(side_length):
    # Function to calculate the area of a rectangle
    def rectangle_area(length, width):
        return length * width

    # A cube has 6 faces and each face is a square (a type of rectangle)
    # So we can use the rectangle_area function to find the area of one face
    # and then multiply it by 6 to get the total surface area of the cube
    return 6 * rectangle_area(side_length, side_length)

# write a function that finds the area of a sphere

import math

def sphere_area(radius):
    return 4 * math.pi * (radius ** 2)
# hint: you can get `pi` by importing math (google it!)
