#!/usr/bin/env python3
#
# Given an integer n, return the number of trailing zeroes in n!.
# Note: Your solution should be in logarithmic time complexity.

def trailing_zeroes(n):
    power_of_5 = 1
    num_trailing_zeroes = 0
    while n // 5 ** power_of_5: 
        num_trailing_zeroes += n // 5 ** power_of_5
        power_of_5 += 1

    return num_trailing_zeroes

# Tests
print(trailing_zeroes(0))
print(trailing_zeroes(1))
print(trailing_zeroes(5))
print(trailing_zeroes(10))
print(trailing_zeroes(24))
print(trailing_zeroes(25))
print(trailing_zeroes(124))
print(trailing_zeroes(125))
print(trailing_zeroes(126))
print(trailing_zeroes(2135684))
print()

# Time complexity
from timeit import Timer
import math

for n in [1, 10, 100, 1000, 10000]:
    t1 = Timer('trailing_zeroes(n)', 
               'from __main__ import trailing_zeroes, n')
    time = t1.timeit(number=10000)
    if n == 1:
        time_1 = time
    ratio = time / time_1
    print('10^{0:1d}  {1:.4f} {2:5.1f}'.format(round(math.log(n, 10)), 
                                              time, ratio))

