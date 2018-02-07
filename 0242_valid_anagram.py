#!/usr/bin/env python3
#
# Given two strings s and t, write a function to determine if t is an anagram i
# of s.
#
# For example,
#   s = "anagram", t = "nagaram", return true.
#   s = "rat", t = "car", return false.
#
# Note: You may assume the string contains only lowercase alphabets.

def _char_count(s):
    ''' takes a string, returns a dictiony of character counts '''
    s_ct = {}
    for char in s:
        if char not in s_ct:
            s_ct[char] = 1
        else:
            s_ct[char] += 1
    return s_ct

def is_anagram(s, t): 
    # Without using imports
    return _char_count(s) == _char_count(t)



def is_anagram_firstattempt(s, t): 
    from collections import Counter
    return Counter(s) == Counter(t)


# Tests
print(is_anagram('anagram', 'nagaram'))
print(is_anagram('rat', 'car'))
    
