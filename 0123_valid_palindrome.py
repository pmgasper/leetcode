#!/usr/bin/env python3
#
# Given a string, determine if it is a palindrome, considering only alphanumeric
# characters and ignoring cases. 
#   For example:
#     "A man, a plan, a canal: Panama" is a palindrome.
#     "race a car" is not a palindrome.


def is_palindrome(s):

    left_idx = 0
    right_idx = len(s) - 1

    while left_idx < right_idx:
        while left_idx < right_idx and not s[left_idx].isalnum():
            left_idx += 1
        while left_idx < right_idx and not s[right_idx].isalnum():
            right_idx -= 1
        
        if s[left_idx].lower() != s[right_idx].lower():
            return False
        else:
            left_idx += 1
            right_idx -= 1

    return True


# Tests
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))
print(is_palindrome("race car"))
print(is_palindrome("::::::"))
print(is_palindrome(":a:::::a"))
print(is_palindrome("a:::a:"))
print(is_palindrome(""))
print(is_palindrome("!#$"))

