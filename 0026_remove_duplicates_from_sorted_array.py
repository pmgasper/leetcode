#!/usr/bin/env python3
#
# Given a sorted array, remove the duplicates in-place such that each element
# appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying 
# the input array in-place with O(1) extra memory.


# iterate through array
# track next idx to fill
#       last number added
# if current number != last number
#    add and increment


def remove_duplicates(nums):
    if not nums:
        return 0

    open_idx = 1
    for idx in range(1, len(nums)):
        if nums[idx] != nums[open_idx - 1]:
            nums[open_idx] = nums[idx]
            open_idx += 1
    nums = nums[:open_idx]
    
    return len(nums)


def remove_duplicates_firstattempt(nums):
    if not nums:
        return 0

    open_idx = 1
    prev_num = nums[0]
    for num in nums[1:]:
        if num != prev_num:
            nums[open_idx] = num
            open_idx += 1
            prev_num = num
    nums = nums[:open_idx]
    
    return len(nums)



# Tests 
print(remove_duplicates([1, 1, 2]))
print(remove_duplicates([]))
print(remove_duplicates([1]))
print(remove_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]))
