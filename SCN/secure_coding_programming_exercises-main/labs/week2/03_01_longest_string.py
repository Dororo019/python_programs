# Which of the following strings is the longest?
# Use the len() function to find out.
# You can run `len(my_variable)` and it will return the len of the variable (in this case it's a string)

longest_german_word = "Donaudampfschifffahrtsgesellschaftskapitänskajütentürschnalle"
longest_hungarian_word = "Megszentségteleníthetetlenségeskedéseitekért"
longest_finnish_word = "Lentokonesuihkuturbiinimoottoriapumekaanikkoaliupseerioppilas"
strong_password = "%8Ddb^ca<*'{9pur/Y(8n}^QPm3G?JJY}\(<bCGHv^FfM}.;)khpkSYTfMA@>N"
# merged a list of strings into one variable
list_of_strings = [longest_german_word, longest_hungarian_word, longest_finnish_word, strong_password]
print(list_of_strings)

# len() function is used here to find out the length of the string
len_strings = [len(my_variable) for my_variable in list_of_strings]
print(len_strings)

# here we are using max() function inside a index function to find out the longest string in the given list
longest_index = len_strings.index(max(len_strings))

longest_string = list_of_strings[longest_index]
print("Longest word length is : ", len(longest_string))

# Now that you know what the longest word is, print it out in an f-string below
print(f"The Longest word from given list of variables  is : ",{longest_string})

