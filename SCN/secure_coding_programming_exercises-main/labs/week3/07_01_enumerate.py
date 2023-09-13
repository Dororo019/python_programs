# use a for loop with enumerate to go over the long word and
# sum all the indices for every single vowel

# example:
#
# input: "hi I me
# i=1, I=3, e = 6,
# the sum is: 10

a_long_word = "the quick brown fox jumped over the lazy dog and then ran around and got very happy happy happy yes!"
# the sum should be 1147 (you can check your code with this)
word_list = []
for word in range(len(a_long_word)):
    if a_long_word[word] in "aeiou":
        word_list.append(word)
 
# printing result
print("The vowel indices are : " + str(word_list))
sum = sum(word_list)
print("Sum of the  vowel indices:",sum)