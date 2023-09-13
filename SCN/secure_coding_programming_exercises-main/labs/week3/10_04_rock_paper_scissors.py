# write rock-paper-scissors game
print('Rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")

# have the user play against the computer
# you can use the random library to select an option for the computer

# use a while loop so the user can play until they win
import random

while True:
   print("Now please enter your choice no. \n 1. Rock \n 2. Paper \n 3. Scissor \n")
# let's give the Input from the user
   your_choice = int(input("Now Your turn: "))

   while your_choice> 3 or your_choice< 1:
      your_choice = int(input("Enter your valid input here: "))
   if your_choice == 1:
      choice_name = 'Rock'
   elif your_choice == 2:
      choice_name = 'Paper'
   else:
      choice_name = 'Scissor'

# print user given choice
   print("Your choice is: " + choice_name)
   
   print("\nNow let give computer to begin the game by entering the choice:")
   
   computer_choice = random.randint(1, 3)
   while computer_choice == your_choice:
      computer_choice = random.randint(1, 3)

   

# you can map each of rock / paper / scissors to an integer from 1 - 3
      if computer_choice == 1:
        computer_choice_name = 'Rock'
      elif computer_choice == 2:
        computer_choice_name = 'Paper'
      else:
        computer_choice_name = 'Scissor'
        print("So computer choice is: " +computer_choice_name)
        
   print(choice_name + " V/s " +computer_choice_name)

# condition for winning the game
   if((your_choice == 1 and computer_choice == 2) or (your_choice == 2 and computer_choice ==1 )):
    print("Paper wins!!!!", end = "")
    final_result = "Paper"
   elif((your_choice == 1 and computer_choice == 3) or (your_choice == 3 and computer_choice == 1)):
      print("Rock wins!!!!", end = " ")
      final_result = "Rock"
   elif((your_choice == 2 and computer_choice == 3) or (your_choice == 3 and computer_choice == 2)):
      print("Scissor wins!!!!", end = " ")
      final_result = "Scissor"
   else:
      print("It's a tie", end = " ")
# Printing either user or computer wins
   
   if final_result == choice_name:
      print("!!!!!!________You are the winner______!!!!!!")
   else:
      print("!!!!!!!!____Computer wins___!!!!!!!!")

   ans = input("Do you want to play again? (Y/N)")
      
# if user input n or N then condition is True
   if ans == 'n' or ans == 'N':
            break
