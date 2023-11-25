# debug this code
# I broke all kinds of things. NOTHING is safe !!!


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
# [1, 2, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 'shiva', 10, 1,2,8,9, "Devi", 10.0, 1, 2]

many_nests = ["a", ["bb", ["ccc", "ddd"], "ee", "ff"], "g", "h"]
# should get back
# ['a', 'bb', 'ccc', 'ddd', 'ee', 'ff', 'g', 'h']


def deep_flatten(any_list):
    while True:
        final_list=[]
        for element in any_list:
            if isinstance(element, (list, tuple)):
                final_list.extend(element)
                # print(final_list)
            else:
                final_list.append(element)  # string,
                
        any_list = final_list
        if not any(isinstance(i, (list, tuple)) for i in any_list):
            break
    return any_list
            # print(final_list)
            # for elem in final_list:
            #     if isinstance(elem, (tuple, list)):
            #         hard_nested_list = []
            #         # hard_nested_list=final_list
            #         
                    
            #         break  # the else below will not execute, we repeat the while loop
        
        # print(final_list)
        # # else:  # no break!!! only executes if for loop finishes
        # break
        
print(deep_flatten(hard_nested_list ))
print(deep_flatten(many_nests))