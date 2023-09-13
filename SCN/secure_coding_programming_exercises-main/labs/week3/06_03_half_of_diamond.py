#Exercise

#Write a Python program to construct the following pattern, using a nested for loop.
"""
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
"""
star = int(input("enter the rows i want:"))

for i in range(star):
    for j in range(0, i + 1):
        print("*", end = '')
    print()
  
    # Loop to print the lower half
    # diamond pattern
for i in range(1, star):
    for j in range(i, star):
            print("*", end = '')
    print()
  




