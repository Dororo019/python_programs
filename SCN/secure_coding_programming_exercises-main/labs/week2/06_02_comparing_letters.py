# can you figure out the logic here?

ay = "a"
bee = "b"

# which one is bigger? bee
string_list = [ay,bee]
print("the biggest",max(string_list))

# why?? Because the ASCII value of b is bigger than a

# here is a hint: check out the ord() function
print(ord(ay))
print(ord(bee))
# How does python store string characters under the hood?In python, everything is object thus an entire object is stored in the heap memory
# look up what ord() does online and report back! it's a built in function in python which returns the number representing the unicode code of a specified character.
# This function accepts a string of unit length as an argument and returns the Unicode equivalence of the passed argument.
# Suppose,a string of length 1, the ord() function returns an integer representing the Unicode code point of the character 
# when an argument is a Unicode object or the value of the byte when the argument is an 8-bit string.