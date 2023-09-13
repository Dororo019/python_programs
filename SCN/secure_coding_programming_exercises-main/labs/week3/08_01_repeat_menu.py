# Exercise

# Write an explicit infinite loop
# inside the infinite loop, read integer from user as an option

# If the option is 1: print here is your first step
# If the option is 2: print "you have some steps to go"
# If the option is 3: print "you are almost done"
# If the option is 4: quit from the loop

# If the option is other number: print it is an  invalid option

while(True):
    option = int(input("Choose any option from 1 to 4:"))
    while option> 4 or option< 1:
      option = int(input("Enter your valid input here: "))
    if option == 1:
        print("here is your first step")
    elif option == 2:
        print("you have some steps to go")
    elif option == 3:  
        print("you are almost done")
    else:
        break
    