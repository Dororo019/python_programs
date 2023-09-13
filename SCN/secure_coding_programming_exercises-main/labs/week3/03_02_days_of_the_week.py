#Exercise

#Write a python program in which read an integer number less than 7 from user

#If the input number is greater than  or equal to 7, then print error message

#If the input is 0 print "Sunday"
#If the input is 1 print "Monday"
#If the input is 2 print "Tuesday"
#If the input is 3 print "Wednesday"
#If the input is 4 print "Thrusday"
#If the input is 5 print "Friday"
#If the input is 6 print "Saturday"

#Use if-else statements
pick_num = int(input("Pick any number between 0 to 6:"))
if pick_num == 0:
    print("Sunday")

elif pick_num == 1:
    print("Monday")

elif pick_num == 2:
    print("Tuesday")

elif pick_num == 3:
    print("Wednesday")

elif pick_num == 4:
    print("Thursday")

elif pick_num == 5:
    print("Friday")

elif pick_num == 6:
    print("Saturday")

else:
    print("error")
    
