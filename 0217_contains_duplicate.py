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
bestcase = [1, 1]
bestcase.extend(range(3, 1000))
bestcase_10x = [1, 1]
bestcase_10x.extend(range(3, 10000))

print('Best case (early duplicate):')
t1 = Timer('contains_duplicate_firstattempt(bestcase)',
           'from __main__ import contains_duplicate_firstattempt, bestcase')
print(' Time first attempt       {0:.5f}'.format(t1.timeit(100)))
t1 = Timer('contains_duplicate_firstattempt(bestcase_10x)',
           'from __main__ import contains_duplicate_firstattempt, bestcase_10x')
print(' Time first attempt 10x   {0:.5f}'.format(t1.timeit(100)))

t2 = Timer('contains_duplicate(bestcase)',
           'from __main__ import contains_duplicate, bestcase')
print(' Time second attempt      {0:.5f}'.format(t1.timeit(100)))

t2 = Timer('contains_duplicate(bestcase_10x)',
           'from __main__ import contains_duplicate, bestcase_10x')
print(' Time second attempt 10x  {0:.5f}'.format(t1.timeit(100)))


print()
worstcase = range(1, 1000)
worstcase_10x = range(1, 10000)
worstcase_100x = range(1, 100000)
t1 = Timer('contains_duplicate_firstattempt(worstcase)',
           'from __main__ import contains_duplicate_firstattempt, worstcase')
print('Worst case (no duplicate):')
print(' Time first attempt       {0:.5f}'.format(t1.timeit(100)))
t1 = Timer('contains_duplicate_firstattempt(worstcase_10x)',
        'from __main__ import contains_duplicate_firstattempt, worstcase_10x')
print(' Time first attempt  10x  {0:.5f}'.format(t1.timeit(100)))
t1 = Timer('contains_duplicate_firstattempt(worstcase_100x)',
        'from __main__ import contains_duplicate_firstattempt, worstcase_100x')
print(' Time first attempt 100x  {0:.5f}'.format(t1.timeit(100)))

t2 = Timer('contains_duplicate(worstcase)',
           'from __main__ import contains_duplicate, worstcase')
print(' Time second attempt      {0:.5f}'.format(t1.timeit(100)))
t2 = Timer('contains_duplicate(worstcase_10x)',
           'from __main__ import contains_duplicate, worstcase_10x')
print(' Time second attempt  10x {0:.5f}'.format(t1.timeit(100)))
t2 = Timer('contains_duplicate(worstcase_100x)',
           'from __main__ import contains_duplicate, worstcase_100x')
print(' Time second attempt 100x {0:.5f}'.format(t1.timeit(100)))


