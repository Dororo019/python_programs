# Type Casting Exercise

a = 3

# 1. print the type of the variable
print(type(a))
#   Convert integer variable to float and confirm the type cast worked (print it out)
my_float= float(a)
print(type(my_float))

# 2. Now, Convert your float variable to string and print out the type
new_string= str(my_float)
print(type(new_string))

# 3. Finally, Convert your string variable back to integer and print it out (the type)
a=int(float(new_string))
print(type(a))
