# Make your list flatten code do a DEEP flatten and account for other datatypes
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
# should get back
# [1, 2, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 'brandon', 10, 10.0, 1, 2]


def list_flat(list_of_lists):
    while any(isinstance(i, (list, tuple)) for i in list_of_lists):
        list_of_lists = [item for sublist in list_of_lists for item in (sublist if isinstance(sublist, (list, tuple)) else [sublist])]
    return list_of_lists


flattened_list = list_flat(hard_nested_list)
print(flattened_list)

many_nests = ["a", ["bb", ["ccc", "ddd"], "ee", "ff"], "g", "h"]
# should get back
# ['a', 'bb', 'ccc', 'ddd', 'ee', 'ff', 'g', 'h']
print(list_flat(many_nests))