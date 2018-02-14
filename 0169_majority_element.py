#!/usr/bin/env python3
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times. You may assume that the 
# array is non-empty and the majority element always exist in the array.


def majority_element_secondattempt(nums): 
    
    # Idea was to improve time complexity, but it looks like sorted is already
    # O(n). Possibly because it is using lazy sorting?. Sorted function is also
    # faster, probably due to C optimization. 

    from collections import defaultdict
    num_count = defaultdict(int)

    for num in nums:
        num_count[num] += 1
        if num_count[num] >= (len(nums) + 1) // 2:
            return num


def majority_element_firstattempt(nums):
    return sorted(nums)[(len(nums) // 2)]


# Tests
print(majority_element_firstattempt([2,1,1,1]))
print(majority_element_firstattempt([1,2,1,1]))
print(majority_element_firstattempt([1,1,2,1]))
print(majority_element_firstattempt([1,1,1,2]))
print(majority_element_firstattempt([1,1,2,2,1]))
print(majority_element_firstattempt([1,2,2,1,1]))


# Time complexity
print()
from timeit import Timer

def time_complex_test(function_name, testlist_name, num_reps = 100):
    t1 = Timer('{0}({1})'.format(function_name, testlist_name),
               'from __main__ import {0}, {1}'.format(function_name,
                                                      testlist_name))
    return t1.timeit(number = num_reps)

test_worstcase = [1] * 100 + [2] * 100 + [1]
test_worstcase_10x = [1] * 1000 + [2] * 1000 + [1]
test_worstcase_100x = [1] * 10000 + [2] * 10000 + [1]

function_name = 'majority_element_secondattempt'
print(function_name)

arg_name = 'test_worstcase'
time = time_complex_test(function_name, arg_name)
print('  time for {0:20}: {1:6.5f}'.format(arg_name, time))

arg_name = 'test_worstcase_10x'
time = time_complex_test(function_name, arg_name)
print('  time for {0:20}: {1:6.5f}'.format(arg_name, time))

arg_name = 'test_worstcase_100x'
time = time_complex_test(function_name, arg_name)
print('  time for {0:20}: {1:6.5f}'.format(arg_name, time))

print()

function_name = 'majority_element_firstattempt'
print(function_name)

arg_name = 'test_worstcase'
time = time_complex_test(function_name, arg_name)
print('  time for {0:20}: {1:6.5f}'.format(arg_name, time))

arg_name = 'test_worstcase_10x'
time = time_complex_test(function_name, arg_name)
print('  time for {0:20}: {1:6.5f}'.format(arg_name, time))

arg_name = 'test_worstcase_100x'
time = time_complex_test(function_name, arg_name)
print('  time for {0:20}: {1:6.5f}'.format(arg_name, time))

print()

