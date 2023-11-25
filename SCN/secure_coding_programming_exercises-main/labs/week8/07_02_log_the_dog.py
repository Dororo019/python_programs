"""
Look up how to use the argv module in python
Run this program as command line and use the argv module to indicate the logging level
Write your logging code to have all the levels of severity
Practice using the different levels of severity on your dog code below. be creative!

"""

import logging

class Dog:
    def __init__(self, limbs=None, eyes=None, color=None, kindness=None):
        self.limbs = limbs
        self.eyes = eyes
        self.color = color
        self.kindness = kindness  # nice, mean, angry, sad, lonely

        ## write some logging code in here
        ## if limbs < 4 -- log a warning! dog needs help (it's missing legs!)
        ## if kindness is sad or lonely, log a warning. If it's mean or angry it's critical! we must be careful
        
        #to configure logging
        logging.basicConfig(level=logging.WARNING)
        
        if self.limbs < 4:
            logging.warning('Dog needs help! It\'s missing legs!')

        # Check the kindness level
        if self.kindness in ['sad', 'lonely']:
            logging.warning('Dog is feeling sad or lonely.')
        elif self.kindness in ['mean', 'angry']:
            logging.critical('Be careful! Dog is mean or angry.')

# we first import the logging module and configure it to log messages with a severity level of WARNING or above. 
# Then in the __init__ method, we check the number of limbs and the kindness level of the dog and log a warning or critical message accordingly. 
# The logging.warning function logs a message with a severity level of WARNING, 
# and the logging.critical function logs a message with a severity level of CRITICAL

if __name__ == "__main__":
    a = Dog(
        limbs=3, eyes=1, color="red", kindness="nice"
    )  # create different dogs and see your logger in action!

     # Create a dog with 4 limbs, 2 eyes, blue color and angry kindness
    b = Dog(limbs=4, eyes=2, color="blue", kindness="angry")

    # Create a dog with 4 limbs, 2 eyes, green color and sad kindness
    c = Dog(limbs=4, eyes=2, color="green", kindness="sad")