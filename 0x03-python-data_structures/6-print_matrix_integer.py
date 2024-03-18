#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for AZ in matrix:
        for WX in AZ:
            print("{:d}".format(WX), end=" " if WX != AZ[-1] else "")
        print()
