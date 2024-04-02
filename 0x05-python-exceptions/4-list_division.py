#!/usr/bin/python3

def list_division(list1, list2, length):
    """Divides two lists element by element.

    Args:
        list1 (list): The first list.
        list2 (list): The second list.
        length (int): The number of elements to divide.

    Returns:
        A new list of length length containing all the divisions.
    """
    new_list = []
    for i in range(0, length):
        try:
            div = list1[i] / list2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)
