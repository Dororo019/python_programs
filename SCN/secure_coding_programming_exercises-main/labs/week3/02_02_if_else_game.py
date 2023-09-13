# write a short command line game
user_name=input("Enter your username:")
# 1. ask the user for their name: (use the input() function)
print("Hello!!!",user_name)
# Say hello to them with their name
# If their name begins with a vowel say something funny about that ("Aha! Oho! Uhu! Ihi! etc", your name begins with a vowel!)
# If their n ame begins with a consonant make an even better joke about it.

vowel = ('a', 'e', 'i', 'o', 'u')
if user_name.startswith((vowel)):
# user_name.startswith(('a', 'e', 'i', 'o', 'u'))
    print("Aha!!Do you know why did the student eat his homework??......Because his teacher told him it would be a piece of cake.LOL2!!ROFL s*@k$ right!! back right at ya for inserting your name like a weeb guy #curiosity bring you here eh?!?potatoie")
else:
    print("WOW!! I see a genius out here, do you only smart people can read these four words four times really fast:[EYE,YAM,STEW,PEED]....................YOU ARE REALLY A GEM!!RIP boiling water,you will be mist")

# Ask them to pick a number between 1 and 10.
# If they guessed the right number, tell them they won
# Else, tell them they lost.

import random

random_number = random.randint(0,10)
print("CRAZY PIN:",random_number)

pick_num =int(input("Pick any number from 0 to 10:"))
if pick_num == random_number:
     print("You won!you guessed the right number!",user_name)
else:
    print("Sorry you lost your lucky chance",user_name)