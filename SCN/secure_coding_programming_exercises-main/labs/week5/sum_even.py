def sum_even_keys(d):
    total = 0
    for key in d:
        if key % 2 == 0:
            total += d[key]
    return total

# Example usage
my_dict = {1: 10, 2: 70, 3: 30, 4: 40}
result = sum_even_keys(my_dict)
print(result)  # Output: 60
