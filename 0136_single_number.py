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
worstcase = [i for i in range(1000)] * 2 + [1000] 
worstcase_10x = [i for i in range(10000)] * 2 + [10000] 
worstcase_100x = [i for i in range(100000)] * 2 + [100000] 
print(singlenumber(worstcase))
print()

# Time complexity
from timeit import Timer

print('singlenumber second attempt')
t1 = Timer('singlenumber(worstcase)', 
           'from __main__ import singlenumber, worstcase')
print('  worstcase     : {0:.5f}'.format(t1.timeit(number = 100)))
t1 = Timer('singlenumber(worstcase_10x)',
           'from __main__ import singlenumber, worstcase_10x')
print('  worstcase  10x: {0:.5f}'.format(t1.timeit(number = 100)))
t1 = Timer('singlenumber(worstcase_100x)',
           'from __main__ import singlenumber, worstcase_100x')
print('  worstcase 100x: {0:.5f}'.format(t1.timeit(number = 100)))


print()

print('singlenumber first attempt')
t1 = Timer('singlenumber_firstattempt(worstcase)', 
           'from __main__ import singlenumber_firstattempt, worstcase')
print('  worstcase     : {0:.5f}'.format(t1.timeit(number = 100)))
t1 = Timer('singlenumber_firstattempt(worstcase_10x)',
           'from __main__ import singlenumber_firstattempt, worstcase_10x')
print('  worstcase  10x: {0:.5f}'.format(t1.timeit(number = 100)))
t1 = Timer('singlenumber_firstattempt(worstcase_100x)',
           'from __main__ import singlenumber_firstattempt, worstcase_100x')
print('  worstcase 100x: {0:.5f}'.format(t1.timeit(number = 100)))
print()
