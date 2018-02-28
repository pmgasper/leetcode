#!/usr/bin/env python3
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one
# sorted array. Note: You may assume that nums1 has enough space (size that is 
# greater or equal to m + n) to hold additional elements from nums2. The 
# number of elements initialized in nums1 and nums2 are m and n respectively.


def merge_sorted(nums1, m, nums2, n):

    while m and n:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1

    if n:
        nums1[:n] = nums2[:n]


# Tests
nums1 = [3, 4, 5, 0, 0]
m = 3
nums2 = [1, 2]
n = 2
merge_sorted(nums1, m, nums2, n)
print(nums1)


nums1 = [1, 2, 0, 0, 0]
m = 2
nums2 = [3, 4, 5]
n = 3
merge_sorted(nums1, m, nums2, n)
print(nums1)

nums1 = []
m = 0 
nums2 = []
n = 0
merge_sorted(nums1, m, nums2, n)
print(nums1)

nums1 = [1, 3, 5, 0, 0, 0]
m = 3 
nums2 = [1, 3, 5]
n = 3
merge_sorted(nums1, m, nums2, n)
print(nums1)
