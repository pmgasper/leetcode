#!/usr/bin/env python3
#
# Given an array of integers, every element appears twice except for one. Find that single one. Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

def singlenumber(nums):
   return sum(set(nums)) * 2 - sum(nums)


def singlenumber_firstattempt(nums):
    seen_once = set()
    for num in nums:
        if num in seen_once:
            seen_once.remove(num)
        else:
            seen_once.add(num)
    if seen_once:
        return list(seen_once)[0]


# Tests
testlist = [i for i in range(1000)] * 2 + [1000] 
print(singlenumber(testlist))
print()

# Time complexity
from timeit import Timer

t1 = Timer('singlenumber(testlist)', 
           'from __main__ import singlenumber, testlist')
print('time for singlenumber: {0:.4f}'.format(t1.timeit(number = 1000)))

t1 = Timer('singlenumber(testlist)', 
           'from __main__ import singlenumber, testlist')
print('10x time for singlenumber: {0:.4f}'.format(t1.timeit(number = 10000)))

t1 = Timer('singlenumber_firstattempt(testlist)', 
           'from __main__ import singlenumber_firstattempt, testlist')
print('time for singlenumber_firstattempt: {0:.4f}'.format(t1.timeit(number = 
                                                                     1000)))

t1 = Timer('singlenumber_firstattempt(testlist)', 
           'from __main__ import singlenumber_firstattempt, testlist')
print('time for singlenumber_firstattempt: {0:.4f}'.format(t1.timeit(number =
                                                                     10000)))

