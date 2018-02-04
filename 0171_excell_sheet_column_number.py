#!/usr/bin/env python3
#
# Given a column title as appear in an Excel sheet, return its corresponding i
# column number.
#
# For example:
#    A -> 1
#    B -> 2
#    C -> 3
#    ...
#    Z -> 26
#    AA -> 27
#    AB -> 28 

def title_to_num(col_name):
    col_number = 0
    for idx, char in enumerate(col_name[::-1]):
        col_number += (ord(char) - 64) * 26 ** idx
    return col_number


# Tests
print(title_to_num('A'))
print(title_to_num('B'))
print(title_to_num('C'))
print(title_to_num('Z'))
print(title_to_num('AA'))
print(title_to_num('AB'))
print(title_to_num('BB'))  # 54
print(title_to_num('ZMC')) # 17917



