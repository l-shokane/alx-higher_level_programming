#!/usr/bin/python3
import random

# Assign a random signed number to the variable 'number'
number = random.randint(-10, 10)

# Check if the number is positive
if number > 0:
    print("{} is positive".format(number))
# check if negative
elif number < 0:
    print("{} is negative".format(number))
# if zero
else:
    print("0 is zero")
