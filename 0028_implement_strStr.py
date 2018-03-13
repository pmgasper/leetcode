#!/usr/bin/env python3
#
# return the index of the first occurrence of needle in haystack, or -1 if 
# needle is not part of haystack.
#
# example:
#    input: haystack = "hello", needle = "ll"
#    output: 2


def needle_haystack(haystack, needle):

    if not needle:
        return 0

    for h_idx in range(len(haystack) - (len(needle) - 1)):
        for n_idx in range(len(needle)):
            if haystack[h_idx + n_idx] != needle[n_idx]:
                break
            elif n_idx == len(needle) - 1:
                return h_idx 

    return -1


def needle_haystack_builtin(haystack, needle):
    return haystack.find(needle)
 


# Tests
print(needle_haystack('hello', 'll'))  # 2 
print(needle_haystack('0123456789llo', 'll'))  # 10
print(needle_haystack('llo', 'll'))  # 0
print(needle_haystack('helll', 'lll'))  # 2
print(needle_haystack('hell', 'ljl'))  # -1
print(needle_haystack('hell', ''))  # 0
print(needle_haystack('', 'ljl'))  # -1
