#!/usr/bin/python3

def safe_print_division(r, s):
    try:
        tid = r / s
    except (TypeError, ZeroDivisionError):
        tid = None
    finally:
        print("Inside result: {}".format(div))
    return (tid)
