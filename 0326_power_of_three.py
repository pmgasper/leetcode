#!/usr/bin/env python3
#
# Given an integer, write a function to determine if it is a power of three.

def is_power_of_three(n):

    if n <= 0:
        return False

    while n > 1:
        if n % 3 != 0:
            return False
        n = n // 3

    return True


# Tests
print(is_power_of_three(0))
print(is_power_of_three(1))
print(is_power_of_three(3))
print(is_power_of_three(6))
print(is_power_of_three(9))
print(is_power_of_three(27))
print(is_power_of_three(30))


#Let n be the decimal number.
#Let m be the number, initially empty, that we are converting to. We'll be
#composing it right to left.
#Let b be the base of the number we are converting to.
#Repeat until n becomes 0 
# Divide n by b, letting the result be d and the remainder be r. 
#   Write the remainder, r, as the leftmost digit of b. 
#   Let d be the new value of n.
