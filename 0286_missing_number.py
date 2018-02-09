#!/usr/bin/env python3

# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
# find the one that is missing from the array. Your algorithm should run in
# linear runtime complexity. 


def missing_number(nums):
    # Using sets, better than numpy, still slower than formula
    return list(set(range(len(nums) + 1)) - set(nums))[0]


def missing_number_secondattempt(nums):
    # Using numpy arrays - much slower than formula in first attempt
    import numpy as np
    missing = np.array(nums + [0]) 
    full = np.array(range(len(nums) + 1 ))
    return sum(full - missing)


def missing_number_firstattempt(nums):
    return int(len(nums) * ((len(nums) + 1) / 2)) - sum(nums)



# Tests
print(missing_number([3, 0, 1]))
print(missing_number([3, 0, 1, 4]))
print(missing_number([3, 0, 1, 2]))
print(missing_number([0, 4, 3, 1]))
print(missing_number([3, 0, 1, 2, 5, 6]))

print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(missing_number([6, 4, 2, 3, 5, 7, 0, 1, 8]))
print(missing_number([x for x in range(1000) if x != 582]))


# Time complexity

from timeit import Timer
print()


testlist = [x for x in range(1000) if x != 582]


t1 = Timer('missing_number_firstattempt(testlist)',
           'from __main__ import missing_number_firstattempt, testlist')
print('Time for first attempt       {0:4f}'.format(t1.timeit(number=1000)))
print('Time for first attempt 10x   {0:4f}'.format(t1.timeit(number=10000)))
print('Time for first attempt 100x  {0:4f}'.format(t1.timeit(number=100000)))

print()

t2 = Timer('missing_number_secondattempt(testlist)',
           'from __main__ import missing_number_secondattempt, testlist')
print('Time for second attempt      {0:4f}'.format(t2.timeit(number=1000)))
print('Time for second attempt 10x  {0:4f}'.format(t2.timeit(number=10000)))
print('Time for second attempt 10x  bad')

print()
t3 = Timer('missing_number(testlist)',
           'from __main__ import missing_number, testlist')
print('Time for third attempt       {0:4f}'.format(t3.timeit(number=1000)))
print('Time for third attempt 10x   {0:4f}'.format(t3.timeit(number=10000)))
print('Time for third attempt 100x  {0:4f}'.format(t3.timeit(number=100000)))

