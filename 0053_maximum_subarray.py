#!/usr/bin/env python3
#
# Find the contiguous subarray within an array (containing at least one number)
# which has the largest sum.
#
#  For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
#  the contiguous subarray [4,-1,2,1] has the largest sum = 6.


# Question appears to ask for subarray, but actually returns largest sum
  # first attempt method below returns subarray 
  # checking question's rtype and testcases first next time would help clairify 
  # expectations

def max_subarray_firstattempt(nums):
    max_indicies = (0, 0)
    max_sum = nums[0]
    trail_idx = 0
    lead_idx = 1
    cont_sum = nums[0]

    while lead_idx < len(nums):

        if cont_sum < 0:
            trail_idx = lead_idx
            cont_sum = 0

        cont_sum += nums[lead_idx] 

        if max_sum < cont_sum:
            # might want to intelligently break or keep ties
            max_sum = cont_sum
            max_indicies = (trail_idx, lead_idx)

        lead_idx += 1

    return nums[max_indicies[0]:max_indicies[1] + 1]


def max_subarray(nums):
    cont_sum = nums[0] 
    max_sum = nums[0]

    for num in nums[1:]:
        cont_sum = max(num, cont_sum + num)
        max_sum = max(max_sum, cont_sum)

    return max_sum


# Tests
print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
print(max_subarray([-2,1,-3,4,-1,2,1,-5,3,1,1,1]))
print(max_subarray([-2,-1,-3]))
print(max_subarray([-2]))

