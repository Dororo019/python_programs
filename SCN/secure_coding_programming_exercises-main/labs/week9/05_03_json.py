"""
Use JSON to serialize the following dictionary

"""
import json

my_dict = {i: i ** 2 for i in range(10_000)}

# after creating your JSON file, try opening it the file by double clicking it in the explorer
# can you read it ? Why or why not?

#  Serialize and write to a file
with open('my_dict.json', 'w') as f:
    json.dump(my_dict, f)

# use code to load your json file into a new variable
#  Load from a file
with open('my_dict.json', 'r') as f:
    my_dict_loaded = json.load(f)
    
# Convert keys back to integers
my_dict_loaded = {int(k): v for k, v in my_dict_loaded.items()}

# print it out to make sure it's the same.
print(my_dict_loaded)


