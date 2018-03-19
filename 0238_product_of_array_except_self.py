#!/usr/bin/env python3
#
# Given an array of n integers where n > 1, nums, return an array output such
# that output[i] is equal to the product of all the elements of nums except
# nums[i]. Solve it without division and in O(n).
#
#   For example, given [1,2,3,4], return [24,12,8,6].


# One iteration
# track cumulative product from both ends, update neighbors

def prod_excpt_self(nums):
    prods = [1] * len(nums)
    left_cum_prod = 1
    right_cum_prod = 1

    for idx in range(1, len(nums)):
        left_cum_prod *= nums[idx - 1]
        right_cum_prod *= nums[-idx]

        prods[idx] *= left_cum_prod
        prods[-1 - idx] *= right_cum_prod
    
    return prods


# Tests
print(prod_excpt_self([1, 2, 3, 4]))
print(prod_excpt_self([4, 3, 2, 1]))
print(prod_excpt_self([1, 2, 3, 4, 5]))
print(prod_excpt_self([-1, 2, -3, 4, -5]))



