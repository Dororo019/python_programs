"""
Pickle the following class
"""
import pickle
class Car:
    cars_created = 0
    def __init__(self, num_tires = 2, color = "red", gas=True):
        self.num_tires = num_tires
        self.color = color
        self.gas = gas
    
    def is_gas(self):
        return self.gas

    def honk_horn(self):
        print("HONK HONK")
    
    def can_drive(self):
        if self.num_tires == 4:
            return True
        return False


# Create an instance of the Car class
my_car = Car(num_tires=4, color="bluish-purple", gas=True)

# Open a file in binary write mode
with open('car.pkl', 'wb') as file:
# Use the pickle.dump() function to pickle and write the object to the file
    pickle.dump(my_car, file)