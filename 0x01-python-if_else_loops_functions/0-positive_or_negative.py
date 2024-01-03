#!/usr/bin/python3
import random

# Assign the random number to the variable
number = random.randint(-10, 10)

# Check if the number is positive
if number > 0:
    print("{} is positive\n".format(number))

# if the number is negative
elif number < 0:
    print("{} is negative\n".format(number))

# if the number is zero
else:
    print("0 is zero\n")
