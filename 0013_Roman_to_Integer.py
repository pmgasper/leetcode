#!/usr/bin/env python3
#
# Given a roman numeral, convert it to an integer. Input is guaranteed to be 
# within the range from 1 to 3999. 

roman_vals = {'I':   1,
              'V':   5,
              'X':  10,
              'L':  50,
              'C': 100,
              'D': 500,
              'M':1000}


def roman_to_int(roman):
    value = 0
    for idx in range(len(roman) - 1):
        # If numerial to right is larger subtract value otherwise add value
        if roman_vals[roman[idx]] < roman_vals[roman[idx + 1]]:
            value -= roman_vals[roman[idx]]
        else:
            value += roman_vals[roman[idx]]
    # Add the last numerial
    value += roman_vals[roman[-1]]

    return value


# Tests
print(roman_to_int('I'))
print(roman_to_int('IV'))
print(roman_to_int('VI'))
print(roman_to_int('IX'))
print(roman_to_int('X'))
