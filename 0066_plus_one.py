#!/usr/bin/env python3
#
# Given a non-negative integer represented as a non-empty array of digits, plus
# one to the integer.
# 
# You may assume the integer does not contain any leading zeroes, except the 
# number 0 itself. The digits are stored such that the most significant digit 
# is at the head of the list.


# iterate digits from last to first
#   if < 9 add 1 and break
#   if 9 set to zero and continue


def plus_one(digits):

    idx = -1
    while -idx <= len(digits):
        if digits[idx] != 9:
            digits[idx] += 1
            break
        else:
            digits[idx] = 0
            if -idx == len(digits):
                digits.insert(0, 1)
                break
            idx -= 1

    return digits


# Tests
print(plus_one([1, 0, 5]))
print(plus_one([1, 0, 9]))
print(plus_one([1, 9, 9]))
print(plus_one([9, 9, 9]))
print(plus_one([0]))


