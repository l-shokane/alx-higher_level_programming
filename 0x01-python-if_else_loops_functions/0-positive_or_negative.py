#!/usr/bin/python3
import random

# Assign a random signed number to the variable 'number'
number = random.randint(-10, 10)

# Check if the number is positive
if number > 0:
    print(f"{number} is positive\n")
# check if negative
elif number < 0:
    print(f"{number} is negative\n")
# check if zero
else:
    print(f"{number} is zero\n")

