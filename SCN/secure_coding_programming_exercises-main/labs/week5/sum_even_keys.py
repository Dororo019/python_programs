# def sum_even_keys(my_dictionary):
#   counter = 0
#   for i in my_dictionary.keys():
    # if (i % 2 == 0):
    #   counter += my_dictionary[i]
    # return counter
    


# print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
# print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6```

def sum_even_keys(anydict):
    sum = 0
    for key in anydict:
        if key % 2 == 0:
            sum += anydict[key]
            final_sum = sum if sum != 0 else 0


    return final_sum
# print(sum_even_keys({4:"5",43:"342",72:"7"}))