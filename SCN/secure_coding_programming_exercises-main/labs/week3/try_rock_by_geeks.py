# importing required random module
import random
print("The Rules of Rock paper scissor game will be follows: \n"
+"Rock vs paper --> paper wins \n"
+"Rock vs scissor --> Rock wins \n"
+"paper vs scissor --> scissor wins \n")
while True:
    print("Now please enter your choice no. \n 1. Rock \n 2. paper \n 3. scissor \n")
    
    choice = int(input("Enter your choice :"))
# take the input from user
    while choice > 3 or choice <1:
      choice=int(input('Enter a valid choice please ☺'))
         
        # initialize value of choice_name variable
    # corresponding to the choice value
    if choice == 1:
        choice_name= 'Rock'
    elif choice == 2:
        choice_name= 'Paper'
    else:
        choice_name= 'Scissors'
         
# print user choice
    print('User choice is \n',choice_name)
    print('Now its Computers Turn....')
     
    # Computer chooses randomly any number
    # among 1 , 2 and 3. Using randint method
    # of random module
    comp_choice = random.randint(1,3)
     
    # looping until comp_choice value
    # is equal to the choice value
    while comp_choice == choice:
        comp_choice = random.randint(1,3)
         
     # initialize value of comp_choice_name
    # variable corresponding to the choice value
    if comp_choice == 1:
        comp_choice_name = 'rocK'
    elif comp_choice == 2:
        comp_choice_name = 'papeR'
    else:
        comp_choice_name = 'scissoR'
    print("Computer choice is \n", comp_choice_name)
    print(choice_name,'Vs',comp_choice_name)
    # we need to check of a draw
    if choice == comp_choice:
        print('Its a Draw',end="")
        result="DRAW"
    # condition for winning     
    if (choice==1 and comp_choice==2):
        print('paper wins =>',end="")
        result='papeR'
    elif (choice==2 and comp_choice==1):
        print('paper wins =>',end="")
        result='Paper'
         
       
    if (choice==1 and comp_choice==3):
        print('Rock wins =>\n',end= "")
        result='Rock'
    elif (choice==3 and comp_choice==1):
        print('Rock wins =>\n',end= "")
        result='rocK'
         
    if (choice==2 and comp_choice==3):
        print('Scissors wins =>',end="")
        result='scissoR'
    elif (choice==3 and comp_choice==2):
        print('Scissors wins =>',end="")
        result='Rock'
     # Printing either user or computer wins or draw
    if result == 'DRAW':
        print("<== Its a tie ==>")
    elif result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")
    # if user input n or N then condition is True
    ans = input("Do you want to play again? (Y/N)")
    if ans =='n' or ans =='N':
        break
# after coming out of the while loop
# we print thanks for playing
print("Thanks for playing")