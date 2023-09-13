# Boolean Exercise_1
# Let's check all the default boolean values of the types we know

# make
# an int
int1 = -1
# a float
float1 = 0.1
# a string
str1 = "TRY" 
# the int 0
int2 = 0
# the int 1
int3 = 1
# the int 1000
int4 = 1000

# now print out all the `bool()` values using the bool() function
print("boolean of an int:",bool(int))
print("boolean int any except 0 is",bool(int1))
print("boolean int 0 is",bool(int2))
print("boolean int 1 is",bool(int3))
print("boolean int 1000 is",bool(int4))
print("boolean of float is",bool(float))
print("boolean float any except 0 is",bool(float1))
print("boolean of string:",bool(str))
print("boolean of newstr is",bool(str1))

# are you surprised at the default boolean value for any python type? 
print(bool())
exit()
# Yes,sir