# Write a script that takes the following two dictionaries
# and creates a new dictionary by combining the common keys
# and adding the values of duplicate keys together.
# Use `for` loops to iterate over these dictionaries
# to accomplish this task.
#
# Example output:
# result = {"a": 3, "b": 2, "c": 7 , "d": 2}

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4, "d": 2}
samekey_dic= {same_key:dict_1[same_key] + dict_2[same_key] for same_key in dict_2 if same_key in dict_1} 
dif1key_dic = {key:dict_1[key] for key in dict_1 if key not in dict_2}
dif2key_dic  = {key:dict_2[key] for key in dict_2 if key not in dict_1}

# print(samekey_dic)
# print(dif1key_dic)
# print(dif2key_dic)

final_dic = samekey_dic|dif1key_dic|dif2key_dic
print(final_dic)

# final_dic =samekey_dic.update(leftover_key_dic)
# print(samekey_dic)
# print(leftoverkey_dic)

# for same_key in dict_2:
    # if same_key in dict_1:
        # final_dic[same_key] = dict_2[same_key] + dict_1[same_key]
    # else:
        # final_dic[same_key]=dict_2[same_key]        



# {keys: keys in dict_1 for keys in dict_2 if keys in dict_1}
