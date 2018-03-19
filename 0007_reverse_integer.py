#!/usr/bin/env python3
#
# Given a 32-bit signed integer, reverse digits of an integer. Assume we are
# dealing with an environment which could only hold integers within the 32-bit
# signed integer range. For the purpose of this problem, assume that your
# function returns 0 when the reversed integer overflows.

def reverse_integer(x):
    sign = ('{0:+d}'.format(x)[0])
    rev_digits = ('{0:+d}'.format(x)[:0:-1])
    rev_x = int(sign + rev_digits)

    if abs(rev_x) < 2 ** 31 - 1:
        return rev_x
    else:
        return 0


# Tests
print(reverse_integer(123))
print(reverse_integer(-123))
print(reverse_integer(120))
print(reverse_integer(1200))
print(reverse_integer(7463847412))
print(reverse_integer(6463847412))
print(reverse_integer(-7463847412))
print(reverse_integer(-6463847412))

