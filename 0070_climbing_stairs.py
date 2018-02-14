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
        return (climb_stairs_firstattempt(n - 1) + 
                climb_stairs_firstattempt(n - 2))
    

def climb_stairs_secondattempt(n, ways={1:1, 2:2}):
    # recursion w/ memorization
    # ways = dictionary of the number of ways to the top (values) from the
    #        stair n from the top (keys)
    if n not in ways:
        ways[n] = (climb_stairs_secondattempt(n - 1) + 
                   climb_stairs_secondattempt(n - 2))

    return ways[n]


def climb_stairs_thirdattempt(n):
    # dynamic programming
    ways = [1, 2]

    if n >= 2:
        for idx in range(2, n):
            ways.append(ways[idx - 2] + ways[idx - 1])
    
    return ways[n - 1]


def climb_stairs_fourthattempt(n):
    # combinatorics
    import math
    num_2s = n // 2
    num_1s = n % 2
    num_ways = 1    # Initial count for way using all 1s
    while num_2s > 0:
        num_ways += (math.factorial(num_2s + num_1s) //
                     (math.factorial(num_2s)  * math.factorial(num_1s)))
        num_2s -= 1
        num_1s += 2

    return num_ways


def climb_stairs_fifthattempt(n):
    # Fibonacci
    import numpy as np
    sqrt5 = np.sqrt(5)
    return int(((((1 + sqrt5) / 2) ** (n + 1)) - 
                (((1 - sqrt5) / 2) ** (n + 1))) / sqrt5)


    
# Tests
print(climb_stairs_fifthattempt(1))
print(climb_stairs_fifthattempt(2))
print(climb_stairs_fifthattempt(3))
print(climb_stairs_fifthattempt(4))
print(climb_stairs_fifthattempt(5))
print(climb_stairs_fifthattempt(35))

    
# Time complexity
from timeit import Timer

def time_complex(funct_str, arg_str, num_reps = 100):
    t1 = Timer('{0}({1})'.format(funct_str, arg_str),
               'from __main__ import {0}, {1}'.format(funct_str, arg_str))
    return t1.timeit(number = num_reps)

arg_str = 'n'

print()
funct_str = 'climb_stairs_firstattempt'
print(funct_str)
for n in [10, 15, 20]:
    time = time_complex(funct_str, arg_str)
    print('  Time for n = {0:5d}: {1:6.4f}'.format(n, time))

print()
funct_str = 'climb_stairs_secondattempt'
print(funct_str)
for n in [10, 100, 1000, 1500]:
    time = time_complex(funct_str, arg_str)
    print('  Time for n = {0:5d}: {1:6.4f}'.format(n, time))
print('  * Note: exceeds maximum recursion depth around 1500')

print()
funct_str = 'climb_stairs_thirdattempt'
print(funct_str)
for n in [10, 100, 1000, 10000, 20000]:
    time = time_complex(funct_str, arg_str)
    print('  Time for n = {0:5d}: {1:6.4f}'.format(n, time))

print()
funct_str = 'climb_stairs_fourthattempt'
print(funct_str)
for n in [10, 100, 500]:
    time = time_complex(funct_str, arg_str)
    print('  Time for n = {0:5d}: {1:6.4f}'.format(n, time))

print()
funct_str = 'climb_stairs_fifthattempt'
print(funct_str)
for n in [10, 100, 1000]:
    time = time_complex(funct_str, arg_str)
    print('  Time for n = {0:5d}: {1:6.4f}'.format(n, time))
print('  * Note: overflow error shortly after 1000')
print()
