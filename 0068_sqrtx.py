#!/usr/bin/env python3
#
# Implement int sqrt(int x). Compute and return the square root of x.
# x is guaranteed to be a non-negative integer.


def int_sqrt(x):
    
    guess = x
    while guess ** 2 > x:
        guess = (guess + x / guess) // 2

    return int(guess)


def int_sqrt_firstattampt(x):
    # Too slow for large numbers, need a more intelligent way to update guess
    guess = x // 2 + 1

    while guess ** 2 > x:
        guess -= 1

    return guess


# Tests
print(int_sqrt(0))
print(int_sqrt(1))
print(int_sqrt(2))
print(int_sqrt(4))
print(int_sqrt(8))
print(int_sqrt(6561))
print(int_sqrt(6514654))
print(int_sqrt(2147395599))
