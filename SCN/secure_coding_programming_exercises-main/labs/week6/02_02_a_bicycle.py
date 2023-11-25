"""
create a simple bicylce class

# Attributes
number of tires
type of of tires (road vs mountain bike)
model
color
number of speeds
brakes (front or back or both)
current speed.

# Methods
brake
pedal faster (should affect speed)
"""
class Bicycle:
# The __init__ method is the constructor that initializes the attributes of the bicycle when a new object is created.
    def __init__(self, tire_type, model, color, speeds, brakes):
        self.num_tires = 2
        self.tire_type = tire_type
        self.model = model
        self.color = color
        self.speeds = speeds
        self.brakes = brakes
        self.current_speed = 0
        
# The brake method decreases the current speed by 1 if the bicycle is moving
    def brake(self):
        if self.current_speed > 0:
            self.current_speed -= 1
            print(f"Hold Your Brakes! Current speed is now {self.current_speed}")
        else:
            print("The bicycle is already stopped.")
            
# The pedal_faster method increases the current speed by 1.
    def pedal_faster(self):
        self.current_speed += 1
        print(f"Pedal faster! Current speed is now {self.current_speed}")



# let's cycle now
my_bike = Bicycle("road", "Trek", "red", 21, "both")
my_bike.pedal_faster()
my_bike.brake()