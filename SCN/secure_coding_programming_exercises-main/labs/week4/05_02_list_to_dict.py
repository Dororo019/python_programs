# Exercise

# Write a Python program to convert the nested list to a list of dictionaries

# Sample lists: [["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]]

# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'},
#                   {'color_name': 'Red', 'color_code': '#FF0000'},
#                   {'color_name': 'Maroon', 'color_code': '#800000'},
#                   {'color_name': 'Yellow', 'color_code': '#FFFF00'}]

# use a for-loop
list1= [["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]]
key_list =["color name:","color_code:"]
# first i created the separate list for colour and its value codes
colours = list1[0]
codes = [list(items) for items in zip(*list1[1:])]
# we each colour and each value from two lists we enumerate another list which contains a string that represents them

for col,code in (zip(colours,codes)):
    print([{key_list[i]: col for i, col in enumerate(pair)} for pair in zip(colours,codes)]) 
    break


# res = dict(zip(keys,values))
# print(res)



