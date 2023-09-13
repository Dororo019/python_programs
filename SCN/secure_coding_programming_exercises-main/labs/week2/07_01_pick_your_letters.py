# Use string indexing and string concatenation (or f-strings)
# to write the sentence "we see trees" only by picking
# the necessary letters from the given string.

word = "tweezers "

w1 = word[1:3]
print(w1)

w2 = word[-2:-8:-2]
print(w2)

w3 = word[0]+word[-3:-2]+word[2:7:3]+word[-2:-1]
print(w3)
 
print("the final word:",w1 +" "+w2 +" "+w3)
 
 
 