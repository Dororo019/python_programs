# Write a script that creates a dictionary of keys, `n`
# and values `n * n` for numbers 1 to 10. For example:
# result = {1: 1, 2: 4, 3: 9, ... and so on}

# Use a comprehension to make this easy

# for n in range(1,10):
print(dict([(n,n**2) for n in range(1,10)]))