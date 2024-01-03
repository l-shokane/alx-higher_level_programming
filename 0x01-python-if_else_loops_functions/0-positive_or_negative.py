#!/usr/bin/python3
import random

# Assign a random signed number to the variable 'number'
number = random.randint(-10, 10)

# Check if the number is positive, negative, or zero
if number > 0:
    print("{} is positive".format(number))
elif number < 0:
    print("{} is negative".format(number))
else:
    print("0 is zero\n")
