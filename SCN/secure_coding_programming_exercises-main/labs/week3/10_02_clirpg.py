# Build a CLI RPG game following the instructions from the course.

# Ask the player for their name.
user_name =int(input("What's your name:"))
# Display a message that greets them and introduces them to the game world.
print("WELCOME TO THE PARADISE",user_name,"!!!")
# Present them with a choice between two doors.
while True:
   print("Now please enter your choice no. \n LEFT  \nRIGHT \n")
# let's give the Input from the user
   your_choice = int(input("Now Your turn: "))
# If they choose the left door, they'll see an empty room
while your_choice==left or your_choice == right:
        your_choice = int(input("Enter your valid input here: "))
   if your_choice == left:
      choice_name = ''
   
# If they choose the right door, then they encounter a dragon.
elif your_choice == 2:
      choice_name = 'Paper'
# In both cases, they have the option to return to the previous room or interact further.
else:
    break
# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.

# When encountering the dragon, they have the choice to fight it.

# If they have the sword from the other room, then they will be able to defeat it and win the game.

# If they don't have the sword, then they will be eaten by the dragon and lose the game.
