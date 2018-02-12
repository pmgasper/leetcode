#!/usr/bin/env python3
#
# You are climbing a stair case. It takes n steps to reach to the top. 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can 
# you climb to the top? Note: Given n will be a positive integer.
#
# Ex. n = 3 -> output = 3 
#   1. 1 step + 1 step + 1 step
#   2. 1 step + 2 steps
#   3. 2 steps + 1 step

def climb_stairs_firstattempt(n):
    # recursion - works but exceeds timelimit for large cases
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return climb_stairs(n - 1) + climb_stairs(n - 2)


def climb_stairs(n, from_stair_n={}):

    # recursion w/ memorization or dynamic programming
    

    pass


# Tests
print(climb_stairs(1))
print(climb_stairs(2))
print(climb_stairs(3))
print(climb_stairs(4))
print(climb_stairs(5))
print(climb_stairs(35))

    
