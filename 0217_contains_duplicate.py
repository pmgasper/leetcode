#!/usr/bin/env python3
#
# Given an array of integers, find if the array contains any duplicates. Your
# function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.


def contains_duplicate(nums):
    return len(set(nums)) != len(nums)


def contains_duplicate_firstattempt(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False


# Tests
print(contains_duplicate([]))
print(contains_duplicate([1]))
print(contains_duplicate([1, 2]))
print(contains_duplicate([1, 2, 2]))


# Time complexity
from timeit import Timer

print()
testlist1 = [1, 1]
testlist1.extend(range(3, 1000))
t1 = Timer('contains_duplicate_firstattempt(testlist1)',
           'from __main__ import contains_duplicate_firstattempt, testlist1')
print('Early duplicate:')
print(' Time first attempt       {0:.4f}'.format(t1.timeit(100)))
print(' Time first attempt  10x  {0:.4f}'.format(t1.timeit(1000)))
print(' Time first attempt 100x  {0:.4f}'.format(t1.timeit(10000)))
print()
t2 = Timer('contains_duplicate(testlist1)',
           'from __main__ import contains_duplicate, testlist1')
print(' Time second attempt      {0:.4f}'.format(t1.timeit(100)))
print(' Time second attempt  10x {0:.4f}'.format(t1.timeit(1000)))
print(' Time second attempt 100x {0:.4f}'.format(t1.timeit(10000)))

print()
testlist2 = range(1, 1000)
t1 = Timer('contains_duplicate_firstattempt(testlist2)',
           'from __main__ import contains_duplicate_firstattempt, testlist2')
print('No duplicate:')
print(' Time first attempt       {0:.4f}'.format(t1.timeit(100)))
print(' Time first attempt  10x  {0:.4f}'.format(t1.timeit(1000)))
print(' Time first attempt 100x  {0:.4f}'.format(t1.timeit(10000)))
print()
t2 = Timer('contains_duplicate(testlist2)',
           'from __main__ import contains_duplicate, testlist2')
print(' Time second attempt      {0:.4f}'.format(t1.timeit(100)))
print(' Time second attempt  10x {0:.4f}'.format(t1.timeit(1000)))
print(' Time second attempt 100x {0:.4f}'.format(t1.timeit(10000)))


