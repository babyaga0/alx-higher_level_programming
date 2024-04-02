#!/usr/bin/python3

def print_safe_integer(input_value):
    """Prints an integer using "{:d}".format().

    Args:
        input_value (int): The integer to be printed.

    Returns:
        Returns True if the integer is successfully printed, otherwise False if a TypeError or ValueError occurs.
    """
    try:
        print("{:d}".format(input_value))
        return True
    except (TypeError, ValueError):
        return False

