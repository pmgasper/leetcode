#!/usr/bin/env python3
#
# Given a string, find the first non-repeating character in it and return it's
# index. If it doesn't exist, return -1.


def first_unique_char_thirdattempt(input_string):
    # Note: second attempt is faster
    seen_char = set()
    for idx, char in enumerate(input_string):
        if (char not in seen_char and
            char not in input_string[idx + 1:]):
                return idx
        else:
            seen_char.add(char)
    return -1
    

def first_unique_char_secondattempt(input_string):
    # Using string methods
    import string
    return min([input_string.find(char) for char in string.ascii_lowercase
                if input_string.count(char) == 1] or [-1])


def first_unique_char_firstattempt(string):
    unique_char = set()
    seen_char = set()
    for char in string:
        if char in unique_char:
            unique_char.remove(char)
        elif char not in seen_char:
            unique_char.add(char)
        seen_char.add(char)

    if len(unique_char) == 0:
        return -1
    else:
        for idx, char in enumerate(string):
            if char in unique_char:
                return idx


# Tests
#print(first_unique_char(''))
#print(first_unique_char('a'))
#print(first_unique_char('aabbcc'))
#print(first_unique_char('adabbcc'))
#print(first_unique_char('aabbccd'))
#print(first_unique_char('aabbccccccd'))


# Time complexity
from timeit import Timer

print()

input_string = ('abc') * 1000 + 'd'
input_string_10x = ('abc') * 10000 + 'd'
t1 = Timer('first_unique_char_firstattempt(input_string)',
           'from __main__ import first_unique_char_firstattempt, input_string')
print('First attempt      {0}'.format(t1.timeit(number = 100)))
t1 = Timer('first_unique_char_firstattempt(input_string_10x)',
           ('from __main__ import first_unique_char_firstattempt,'
            'input_string_10x'))
print('First attempt 10x  {0}'.format(t1.timeit(number = 100)))
print()

t2 = Timer('first_unique_char_secondattempt(input_string)',
           'from __main__ import first_unique_char_secondattempt, input_string')
print('Second attempt     {0}'.format(t2.timeit(number = 100)))
t2 = Timer('first_unique_char_secondattempt(input_string_10x)',
           ('from __main__ import first_unique_char_secondattempt,' 
            'input_string_10x'))


print('Second attempt 10x {0}'.format(t2.timeit(number = 100)))
print()

t3 = Timer('first_unique_char_thirdattempt(input_string)',
           ('from __main__ import first_unique_char_thirdattempt,'
            'input_string'))
print('Thrid attempt      {0}'.format(t3.timeit(number = 100)))
t3 = Timer('first_unique_char_thirdattempt(input_string_10x)',
           ('from __main__ import first_unique_char_thirdattempt,'
            'input_string_10x'))
print('Thrid attempt 10x  {0}'.format(t3.timeit(number = 100)))
print()
