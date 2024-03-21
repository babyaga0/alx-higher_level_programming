#!/usr/bin/python3

def uniq_add(my_list=[]):

    new_list = []
    SU = 0
    for NU in my_list:
        if NU not in new_list:
            SU += NU
            new_list.append(NU)
    return SU
