#!/usr/bin/env python3
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security system
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each
# house, determine the maximum amount of money you can rob tonight without
# alerting the police.


# For every house, your options are: 
#   rob this house, forgoing previous house, but keeping all profits before 
#   or don't rob this house, keep all profits from robbing previous houses
def rob(houses):
    prev2 = 0  # profit two houses ago
    prev1 = 0  # profit one house ago
    curr = 0   # current profit

    for house in houses:
        curr = max(prev2 + house, prev1)
        prev2 = prev1
        prev1 = curr

    return curr


# First attempt - consider all possibilities with recursion
#   works but too inefficient
def _rob_fa(houses, robbed_neighbor):
    if len(houses) == 1:
        if robbed_neighbor == True:
            return 0
        else:
            return houses[0]

    else:
        if robbed_neighbor == True:
            return max(_rob_fa(houses[1:], True), 
                       _rob_fa(houses[1:], False))
            
        else:
            return max(houses[0] + _rob_fa(houses[1:], True), 
                       _rob_fa(houses[1:], False))

def rob_firstattempt(houses):
    if len(houses) == 1:
        return houses[0]

    return max(houses[0] + _rob_fa(houses[1:], True), _rob_fa(houses[1:], False))


# Tests
print(rob([20, 10, 20]))
print(rob([10, 20, 10]))
print(rob([10, 10, 20]))
print(rob([10, 20, 30]))
print(rob([10, 20, 30, 40]))
print(rob([10, 20, 30, 40, 50]))
print(rob([30, 40, 50, 20, 10]))
print(rob([20]))
