#!/usr/bin/python3

def safe_print_integer(value):
    """Print an integer value.

    Args:
        value (int): The integer to print.

    Returns:
        True - If an integer is printed.
        Otherwise - False
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
