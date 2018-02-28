#!/usr/bin/env python3
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid. The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


def is_valid(s):
    close_pair = {'(': ')', 
                  '[': ']', 
                  '{': '}'}

    stack = []
    for char in s:
        if char in close_pair:
            stack.append(char)
        elif not stack:
            return False
        elif close_pair[stack.pop()] != char:
            return False

    if stack:
        return False
    else:
        return True

# Tests
print(is_valid('()'))
print(is_valid('()[]{}'))
print(is_valid('()[]{}('))
print(is_valid('(]'))
print(is_valid('([)]'))
