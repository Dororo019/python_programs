# Exercise

# stage 1
# Write a program to count the number of strings where the string length is 2 or more
# sample list: ['aaaa', 'a', 'ab', 'abc', ]
# result : 3
word_list1=['aaa','a','ab','abc']

count = 0
for word in word_list1:
     if len(word) > 1 :
        count += 1
        
print("The longest string is:",(len(word)))       

## Stage 2
# Now count the number of strings that have length 2 or more
# AND the first and last character are same from a given list of strings.

# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
word_list2 =['abc','xyz','aba','1221']
c = 0
print("from a given list of strings havinglength 2 or more and the first and last character are same :")
for word in word_list2:
        if len(word) > 1 and word[0] == word[-1]:
                print(word) 
                c+=1
print("The no of strings from a given list having length 2 or more and the first and last character are same:",c)  
           

                
                


# def count_strings(strings):
# count = 0

#    for string in strings:

#        if len(string) >= 2 and string[0] == string[-1]:

        #    count += 1

#    return count

# strings = ['abc', 'xyz', 'aba', '1221']

# result = count_strings(strings)