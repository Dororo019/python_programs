import random

class Hen:
    def __init__(self):
        self.eggs = 0

    def lay_egg(self):
        # Chickens lay eggs based on a random chance
        if random.random() < 0.5:  # 50% chance of laying an egg
            self.eggs += 1

# Create a chicken
chicken = Hen()

# Simulate the chicken laying eggs
for _ in range(10):  # Simulate for 10 days
    chicken.lay_egg()

print(f"The chicken laid {chicken.eggs} eggs.")
