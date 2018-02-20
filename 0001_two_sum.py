#!/usr/bin/env python3
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target. You may assume that each input would have 
# exactly one solution, and you may not use the same element twice.

# Example:
#    Given nums = [2, 7, 11, 15], target = 9, return [0, 1].


def two_sum(nums, target):
    # using hash table - O(n)
    complements = {}    # key = number need to reach target
                        # value = index of complement

    for idx, num in enumerate(nums):
        if num in complements:
            return [complements[num], idx]
        else:
            complements[target - num] = idx


def two_sum_1(nums, target):
    # Brute force - works, but poor time complexity O(n^2) 
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)): 
            if nums[i] + nums[j] == target:
                return [i, j]


# Tests
print(two_sum([2, 7, 11, 15], 9))
print(two_sum([11, 7, 2, 15], 9))
print(two_sum([2, 11, 15, 7], 9))


# Time complexity
from timeit import Timer

# worst case test lists
test_list_1 = list(range(3, 10)) + [1, 2]
test_list_10x = list(range(3, 100)) + [1, 2]
test_list_100x = list(range(3, 1000)) + [1, 2]
test_target = 3

print()
print('two_sum_1')
t1 = Timer('two_sum_1(test_list_1, test_target)',
           'from __main__ import two_sum_1, test_list_1, test_target') 
print('   1x {0:.5f}'.format(t1.timeit(number = 100)))
t1 = Timer('two_sum_1(test_list_10x, test_target)',
           'from __main__ import two_sum_1, test_list_10x, test_target') 
print('  10x {0:.5f}'.format(t1.timeit(number = 100)))
t1 = Timer('two_sum_1(test_list_100x, test_target)',
           'from __main__ import two_sum_1, test_list_100x, test_target') 
print(' 100x {0:.5f}'.format(t1.timeit(number = 100)))

print()
print('two sum')
t1 = Timer('two_sum(test_list_1, test_target)',
           'from __main__ import two_sum, test_list_1, test_target') 
print('   1x {0:.5f}'.format(t1.timeit(number = 100)))
t1 = Timer('two_sum(test_list_10x, test_target)',
           'from __main__ import two_sum, test_list_10x, test_target') 
print('  10x {0:.5f}'.format(t1.timeit(number = 100)))
t1 = Timer('two_sum(test_list_100x, test_target)',
           'from __main__ import two_sum, test_list_100x, test_target') 
print(' 100x {0:.5f}'.format(t1.timeit(number = 100)))
