"""
Import your function from 01_01_sum_ints_inf_args.py
and use it here

Go back into your code and stop your print statements from showing up here

"""
from sum_inf_ints import sum_ints

import sys, os

# Disable print statements
def block_print():
    sys.stdout = open(os.devnull, 'w')

# This won't print anything
block_print()
sum_ints() 

# Enable print statements
def enable_print():
    sys.stdout = sys.__stdout__
    
#will print as usual
enable_print()
sum_ints()  



