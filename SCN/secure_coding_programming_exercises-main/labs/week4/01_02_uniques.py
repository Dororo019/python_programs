# Write code that creates a list of all unique values in a list.
# For example:
#
# list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# unique_list = [1, 2, 6, 55, 'hi', 4, 13,]

# lists given as a example in above
list1=[1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
list2=[1, 2, 6, 55, 'hi', 4, 13,]


unique_nums1 = list(set(list1))
unique_nums2 = list(set(list2))     
print("\nthe unique values from 1st list is",unique_nums1)
        
print("\nthe unique values from 2nd list is",unique_nums2)