#!/usr/bin/env python3
#
# Write a function to find the longest common prefix string amongst an array of
# strings.


def longest_common_prefix_sort(strings):
    # sorting first
    
    if not strings:
        return ''

    strings.sort()
    longest = strings[0]
    for s in strings[1:]:
        for idx in range(len(longest)):
            if longest[idx] != s[idx]:
                longest = s[:idx]
                break

    return longest


def longest_common_prefix_nosort(strings):
    if not strings:
        return ''

    longest = strings[0] 
    for s in strings[1:]:
        if not s:
            return ''
        for idx in range(min(len(longest), len(s))):
            if longest[idx] != s[idx]:
                longest = s[:idx]
                break
            elif idx == min(len(longest), len(s)) - 1:
                longest = s[:idx + 1]

    return longest


# tests
print(longest_common_prefix_sort(['aa', 'a']))
print(longest_common_prefix_sort(['a', 'aa']))
print(longest_common_prefix_sort(['aaa', 'aab', 'aac']))
print(longest_common_prefix_sort(['aba', 'aaa', 'aab']))
print(longest_common_prefix_sort(['aaab', 'aabaa', 'aabaa']))
print(longest_common_prefix_sort(['aaab', 'aabaa', '']))


# time complexity
from timeit import Timer

# Time test 1 - few strings, long similar prefixes
a1000 = 'a' * 1000
test_strs = [a1000 + 'b', a1000 + 'c', a1000 + 'd']

t_sort = Timer('longest_common_prefix_sort(test_strs)',
           'from __main__ import longest_common_prefix_sort, test_strs')
t_nosort = Timer('longest_common_prefix_nosort(test_strs)',
           'from __main__ import longest_common_prefix_nosort, test_strs')

print('Few strings, long similar prefixes')
print(' Sort    {0:.3f}'.format(t_sort.timeit(number=100)))
print(' No sort {0:.3f}'.format(t_nosort.timeit(number=100)))
print()


# Time test 2 - many short strings  
import string
import random
test_strs = [random.choice(string.ascii_lowercase) for _ in range(10000)]

t_sort = Timer('longest_common_prefix_sort(test_strs)',
           'from __main__ import longest_common_prefix_sort, test_strs')
t_nosort = Timer('longest_common_prefix_nosort(test_strs)',
           'from __main__ import longest_common_prefix_nosort, test_strs')

print('Many strings, short similar prefixes')
print(' Sort    {0:.3f}'.format(t_sort.timeit(number=100)))
print(' No sort {0:.3f}'.format(t_nosort.timeit(number=100)))
print()


# Time test 3 - few strings, some long similar prefixes
a1000 = 'a' * 1000
test_strs = [a1000 + 'b', a1000 + 'c', 'd' + a1000]

t_sort = Timer('longest_common_prefix_sort(test_strs)',
           'from __main__ import longest_common_prefix_sort, test_strs')
t_nosort = Timer('longest_common_prefix_nosort(test_strs)',
           'from __main__ import longest_common_prefix_nosort, test_strs')

print('Few strings, some long similar prefixes at begining of list')
print(' Sort    {0:.3f}'.format(t_sort.timeit(number=100)))
print(' No sort {0:.3f}'.format(t_nosort.timeit(number=100)))
print()


