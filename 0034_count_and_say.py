#!/usr/bin/env python3
#
# The count-and-say sequence is the sequence of integers with the first five
# terms as following:
#
#    1.     1
#    2.     11
#    3.     21
#    4.     1211
#    5.     111221
#    1 is read off as "one 1" or 11.
#    11 is read off as "two 1s" or 21.
#    21 is read off as "one 2, then one 1" or 1211.
#
#    Given an integer n, generate the nth term of the count-and-say sequence.
#
#    Note: Each term of the sequence of integers will be a string.


def count_and_say(n):
    say = '1'
    for _ in range(n - 1):
        char = say[0]
        count = 1
        new_say = ''
        prev_char = char
        for char in say[1:]:
            if char == prev_char:
                count += 1
            else:
                new_say += str(count) + prev_char
                count = 1
                prev_char = char
        new_say += str(count) + char
        say = new_say

    return say



# Tests
print(count_and_say(1))
print(count_and_say(2))
print(count_and_say(3))
print(count_and_say(4))
print(count_and_say(5))


