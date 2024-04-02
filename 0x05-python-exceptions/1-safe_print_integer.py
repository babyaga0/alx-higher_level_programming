#!/usr/bin/python3

def safe_print_list(input_list=[], count=0):
    """Prints a specified number of elements from a list.

    Args:
        input_list (list): The list from which elements are to be printed.
        count (int): The number of elements from input_list to print.

    Returns:
        The number of elements printed.
    """
    printed_count = 0
    for i in range(count):
        try:
            print("{}".format(input_list[i]), end="")
            printed_count += 1
        except IndexError:
            break
    print("")
    return printed_count

