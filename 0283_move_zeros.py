#!/usr/bin/env python3
#
# Given an array nums, write a function to move all 0's to the end of it while 
# maintaining the relative order of the non-zero elements. For example, given 
# nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.


def move_zeroes(nums):
    zero_idx = 0
    for idx in range(len(nums)):
        if nums[idx] != 0:
            nums[idx], nums[zero_idx] = nums[zero_idx], nums[idx]
            zero_idx += 1
    return(nums)

def move_zeroes_firstattempt(nums):
    open_idx = 0
    zero_count = 0
    for idx in range(len(nums)):
        if nums[idx] == 0:
            zero_count += 1
        else:
            nums[open_idx] = nums[idx]
            open_idx += 1
        if zero_count >= len(nums) - idx:
           nums[idx] = 0

    return nums


# Tests
print(move_zeroes([0, 1, 0, 3, 12]))
print(move_zeroes([1, 1, 0, 3, 12]))
print(move_zeroes([1]))
print(move_zeroes([]))
            

