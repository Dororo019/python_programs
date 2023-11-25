## write a deep flatten function that works recursively
## earlier we wrote a deep flatten script that would flatten a nested list
## we solved it with an iterative approach (using a for-break loop)
# now solve it with a recursive function!

hard_nested_list = [
    [1, 2, [1, [1, 2], 2], 3, 4],
    [5, 6],
    [7, 8, 9],
    "shiva",
    10,
    [1, 2, [8, 9,], "Devi"],
    10.0,
    (1, 2),
]



def deep_flatten(any_list):
    new_list = []
    for item in any_list:
        if isinstance(item, (list, tuple)):
            new_list.extend(deep_flatten(item))
        else:
            new_list.append(item)
    return new_list


# should get back
# [1, 2, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9,'shiva', 10, 1, 2, 8, 9, 'Devi', 1, 2]

many_nests = ["a", ["bb", ["ccc", "ddd"], "ee", "ff"], "g", "h"]
# should get back
# ['a', 'bb', 'ccc', 'ddd', 'ee', 'ff', 'g', 'h']

print(deep_flatten(many_nests))
flattened_list = deep_flatten(hard_nested_list)
print(flattened_list)
