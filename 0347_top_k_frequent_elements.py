#!/usr/bin/env python3
#
# Given a non-empty array of integers, return the k most frequent elements. 
# For example, Given [1,1,1,2,2,3] and k = 2, return [1,2].

# Note: 
#   You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
#   Your algorithm's time complexity must be better than O(n log n), where n is
#   the array's size.


def top_k_freq_counter(nums, k):
    # using Counter module 
    from collections import Counter
    return [num[0] for num in Counter(nums).most_common(k)]


def top_k_freq(nums, k):
    # only builtins
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    return sorted(count.keys(), key=count.get, reverse=True)[:k]


# Tests
print(top_k_freq([1,1,1,2,2,3], 2))
print(top_k_freq([1,1,1,2,2,3,3,3,3], 2))
print(top_k_freq([3,1,1,2,2,3,4,5], 3))
print(top_k_freq([1], 1))
