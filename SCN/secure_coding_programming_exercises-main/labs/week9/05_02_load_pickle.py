"""
Load your pickled files from 05_01 and use them here!

"""
import pickle
from pickle_car import Car

# # Load the instance of the car
#\ my_car = Car(num_tires=4, color="bluish-purple", gas=True)

# Open a file in binary write mode
with open('her_car.pkl', 'rb') as file:
# Use the pickle.dump() function to pickle and write the object to the file
     that_car=pickle.load(file)
#Let's check the attributes and methods of the car object
print(that_car.num_tires)
print(that_car.color)
print(that_car.gas)
print(that_car.is_gas())
that_car.honk_horn()
print(that_car.can_drive())