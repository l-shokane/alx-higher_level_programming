#!/usr/bin/python3
import random

# Assign a random signed number to the variable 'number'
number = random.randint(-10000, 10000)

# Gets the last digit of the number
last_digit = abs(number) % 10  # Using abs to handle negative numbers

# Format the output
output_string = "Last digit of {} is {} and is {}"

# if greater than
if last_digit > 5:
    output = output_string.format(number, last_digit, "greater than 5")

# if equal to zero
elif last_digit == 0:
    output = output_string.format(number, last_digit, "0")
else:
    output = output_string.format(number, last_digit, "less than 6 and not 0")

# Print output
print(output)
