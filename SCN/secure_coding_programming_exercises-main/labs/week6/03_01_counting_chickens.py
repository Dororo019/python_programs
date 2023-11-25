"""
create a chicken class that has the following

# class attributes
time_of_day
number_of_eggs_laid

# instance attributes (uses the self variable)
breed
gender
weight
lays_eggs (boolean)

# methods
lay_egg --> this function should depend on time of day (chickens only lay eggs at night!),
it should also use random numbers to deterimine if laying the egg worked or not


## Create 100 instances of your chickens using a for loop

Use a for loop to update the time of day (go through each hour of the day)
within the loop have your chickens all try to lay eggs
Afterwards, print out how many total eggs were hatched -- for all chickens and individually.
What was the average number of eggs per chicken?0
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

# raising here 100 chickens
chickens = [Chicken('Breed'+str(i), 'Female', i, True) for i in range(100)]

# In each hour of the day,the chicken tries to lay eggs
for hour in range(24):
    Chicken.time_of_day = hour
    # Have all chickens try to lay eggs
    for chicken in chickens:
        chicken.lay_egg()

# Print out total eggs laid
print(f"Total eggs laid: {Chicken.number_of_eggs_laid}")

# Print out eggs laid per chicken and calculate average
total_eggs = 0
for i, chicken in enumerate(chickens):
    print(f"Chicken {i+1} laid {chicken.eggs_laid} eggs.")
    total_eggs += chicken.eggs_laid

print(f"Average number of eggs per chicken: {total_eggs/len(chickens)}")

