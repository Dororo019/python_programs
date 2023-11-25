"""
Write 3 classes which are related to each other
1) a monster class
2) a night-monster class (they only come out at night)
3) a full moon monster class (they only come out at night and on the full moon)

Make use of inheritance to save your code!

## Monster class
# class attribute
time_of_day (will need to activate night monsters)
day_of_month
full_moon (boolean)

# attributes
name
number of limbs
attack mode (magic, physical, mental hypnosis etc)
scare factor
weakness
life points

# methods
basic attack (attack something)
sleep (get life points back)
defend (something attacks it!)

## Night monster
same as above, but also special powers that activate at night
vulnerable in daylight


## full moon monster
only active in the full moon
"""


class Monster:
    time_of_day = 'day'
    day_of_month = 1
    full_moon = False
# Monster maidaka uni dakbewal features in class attributes
    def __init__(self, name, limbs, attack_mode, scare_factor, weakness, life_points):
        self.name = name
        self.limbs = limbs
        self.attack_mode = attack_mode
        self.scare_factor = scare_factor
        self.weakness = weakness
        self.life_points = life_points

# class  Methods from class MOnster
    def basic_attack(self):
        return f'{self.name} attacks with {self.attack_mode}!'

    def sleep(self):
        self.life_points += 10
        return f'{self.name} sleeps and recovers life points! Now has {self.life_points} life points.'

    def defend(self):
        return f'{self.name} defends with {self.weakness}!'

# subclass of Monster that adds a special_powers attribute 
# and overrides the use_special_powers() method to check if it’s night before using special powers.
class NightMonster(Monster):
    def __init__(self, name, limbs, attack_mode, scare_factor, weakness, life_points, special_powers):
        super().__init__(name, limbs, attack_mode, scare_factor, weakness, life_points)
        self.special_powers = special_powers

    def use_special_powers(self):
        if Monster.time_of_day == 'night':
            return f'{self.name} uses special powers: {self.special_powers}!'
        else:
            return f'{self.name} is vulnerable in daylight and cannot use special powers.'


class FullMoonMonster(NightMonster):
    def __init__(self, name, limbs, attack_mode, scare_factor, weakness, life_points, special_powers):
        super().__init__(name, limbs, attack_mode, scare_factor, weakness, life_points, special_powers)

    def use_special_powers(self):
        if Monster.time_of_day == 'night' and Monster.full_moon:
            return f'{self.name} uses special powers: {self.special_powers}!'
        else:
            return f'{self.name} can only use special powers on a full moon night.'
        
# Update time_of_day to 'night'
Monster.time_of_day = 'night'

# Update day_of_month to 15
Monster.day_of_month = 15

# Update full_moon to True
Monster.full_moon = True



# Create a Monster object
monster = Monster('Monster1', 4, 'physical', 5, 'fire', 100)

# Create a NightMonster object
night_monster = NightMonster('NightMonster1', 4, 'magic', 7, 'light', 120, 'invisibility')

# Create a FullMoonMonster object
full_moon_monster = FullMoonMonster('FullMoonMonster1', 4, 'mental hypnosis', 9, 'silver', 150, 'shape-shifting')

# Call methods of the Monster object
print(monster.basic_attack())
print(monster.sleep())
print(monster.defend())

# Call methods of the NightMonster object
print(night_monster.basic_attack())
print(night_monster.sleep())
print(night_monster.defend())
print(night_monster.use_special_powers())

# Call methods of the FullMoonMonster object
print(full_moon_monster.basic_attack())
print(full_moon_monster.sleep())
print(full_moon_monster.defend())
print(full_moon_monster.use_special_powers())

# Update class attributes to 'night' and True for full moon
Monster.time_of_day = 'night'
Monster.full_moon = True

# Call special powers methods again to see the difference
print(night_monster.use_special_powers())
print(full_moon_monster.use_special_powers())

