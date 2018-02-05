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
import random
print(majority_element_firstattempt([2] + [random.random()] * 100 + [2] * 100))


# Time complexity
print()
from timeit import Timer
import random

def time_complex_test(function_name, testlist_name, num_reps = 1000):
    t1 = Timer('{0}({1})'.format(function_name, testlist_name),
               'from __main__ import {0}, {1}'.format(function_name,
                                                      testlist_name))
    return t1.timeit(number = num_reps)
    

arg_name = 'testlist1'
testlist1 = [2] + [random.random()] * 1000 + [2] * 1000
print(arg_name)

function_name = 'majority_element_secondattempt'

reps = 100
time = time_complex_test(function_name, arg_name, reps)
print('  Time for {0:40} {1:>6}x = {2:6.4f}'.format(function_name, reps, time))

reps = 1000
time = time_complex_test(function_name, arg_name, reps)
print('  Time for {0:40} {1:>6}x = {2:6.4f}'.format(function_name, reps, time))

reps = 10000
time = time_complex_test(function_name, arg_name, reps)
print('  Time for {0:40} {1:>6}x = {2:6.4f}'.format(function_name, reps, time))

print()

function_name = 'majority_element_firstattempt'
reps = 100
time = time_complex_test(function_name, arg_name, reps)
print('  Time for {0:40} {1:>6}x = {2:6.4f}'.format(function_name, reps, time))

function_name = 'majority_element_firstattempt'
reps = 1000
time = time_complex_test(function_name, arg_name, reps)
print('  Time for {0:40} {1:>6}x = {2:6.4f}'.format(function_name, reps, time))

reps = 10000
time = time_complex_test(function_name, arg_name, reps)
print('  Time for {0:40} {1:>6}x = {2:6.4f}'.format(function_name, reps, time))

print()
arg_name = 'testlist2'
testlist2 = [1] * 101 + [2] * 100 + [1]
print(arg_name)

function_name = 'majority_element_secondattempt'
reps = 1000
time = time_complex_test(function_name, arg_name, reps)
print('  Time for {0:40} {1:>6}x = {2:6.4f}'.format(function_name, reps, time))

reps = 10000
time = time_complex_test(function_name, arg_name, reps)
print('  Time for {0:40} {1:>6}x = {2:6.4f}'.format(function_name, reps, time))

function_name = 'majority_element_firstattempt'
reps = 1000
time = time_complex_test(function_name, arg_name, reps)
print('  Time for {0:40} {1:>6}x = {2:6.4f}'.format(function_name, reps, time))

reps = 10000
time = time_complex_test(function_name, arg_name, reps)
print('  Time for {0:40} {1:>6}x = {2:6.4f}'.format(function_name, reps, time))
