#!/usr/bin/env python3
#
# Write an algorithm to determine if a number is "happy". A happy number is a 
# number defined by the following process: Starting with any positive integer, 
# replace the number by the sum of the squares of its digits, and repeat the 
# process until the number equals 1 (where it will stay), or it loops endlessly
# in a cycle which does not include 1. Those numbers for which this process 
# ends in 1 are happy numbers. Example: 19 is a happy number

def _sum_digit_squares(num):
    sq_sum = 0
    for digit in str(num):
        sq_sum += int(digit) ** 2
    return sq_sum

def is_happy(num):
    # Only positive integers can be 'happy' numbers
    if num <= 0:
        return False

    # 'Happy' test
    nums_seen = set([num])
    while True:
        num = _sum_digit_squares(num)
        if num == 1:
            return True
        elif num in nums_seen:
            return False
        else:
            nums_seen.add(num)
    

# Tests
print(is_happy(19))
print(is_happy(0))
print(is_happy(215))
print(is_happy(13))
print(is_happy(651684564684013))

