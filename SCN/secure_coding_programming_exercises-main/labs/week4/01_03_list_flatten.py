#Exercise

# Write a Python program to flatten a shallow list

#Sample Input: [[2,4,3],[1,5,6], [9], [7,9,0]]
#Output: [2, 4, 3, 1, 5, 6, 9, 7, 9, 0]

list_of_lists = [[2,4,3],[1,5,6], [9], [7,9,0]]
flat_list = [item for sublist in list_of_lists for item in sublist]
print("new list:",flat_list)