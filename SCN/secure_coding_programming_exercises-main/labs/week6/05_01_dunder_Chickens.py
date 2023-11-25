"""
Update your chicken class to include the following dunders

__str__  : make some nice str format for your chicken. 
When we print your chicken it should tell us: how heavy the chicken is, the gender and how many eggs it has laid (if has)

__add__ : what happens when you add two chickens together? If they are male and female, create a baby chicken! (a new chicken) Otherwise, nothing?

"""
import random

class Chicken:
    time_of_day = 0
    number_of_eggs_laid = 0

    def __init__(self, breed, gender, weight, lays_eggs):
        self.breed = breed
        self.gender = gender
        self.weight = weight
        self.lays_eggs = lays_eggs
        self.eggs_laid = 0

    def lay_egg(self):
        if self.lays_eggs and Chicken.time_of_day >= 20 and Chicken.time_of_day <= 4:
            if random.random() < 0.5:  # 50% chance of laying an egg
                self.eggs_laid += 1
                Chicken.number_of_eggs_laid += 1

    def __str__(self):
        return f"This is a {self.weight} kg {self.gender} chicken of breed {self.breed}. It has laid {self.eggs_laid} eggs."

    def __add__(self, other):
        if isinstance(other, Chicken) and self.gender != other.gender:
            return Chicken('Mixed Breed', random.choice(['Male', 'Female']), (self.weight + other.weight) / 2, True)
        else:
            return None

# Create two chickens
chicken1 = Chicken('DESI INDIAN', 'male', 2, False)
chicken2 = Chicken('COILAR', 'female', 1, True)

# Print the chickens
print(chicken1)
print(chicken2)

# Add the chickens together to create a baby chicken
baby_chicken = chicken1 + chicken2

# Print the baby chicken
if baby_chicken is not None:
    print("A baby chicken is born!")
    print(baby_chicken)
else:
    print("The chickens cannot have a baby.")

