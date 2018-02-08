#!/usr/bin/env python3
#
# Given two arrays, write a function to compute their intersection.

# Example:
#    Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
#
#    Note:
#        Each element in the result should appear as many times as it shows in
#        both arrays. The result can be in any order.


def array_intersection(num1, nums2):
    from collections import Counter
    inter_count = Counter(nums1) & Counter(nums2)
    return [keylist for key in inter_count
                    for keylist in [key] * inter_count[key]]
    

def array_intersection_secondattempt(nums1, nums2):
    from collections import defaultdict
    nums1_cnt = defaultdict(int)
    
    for num in nums1:
        nums1_cnt[num] += 1
        
    inter_nums = []
    for num in nums2:
        if nums1_cnt[num] > 0:
            inter_nums.append(num)
            nums1_cnt[num] -= 1
            
    return inter_nums


def array_intersection_firstattempt(nums1, nums2):
    nums1.sort()    
    nums2.sort()

    nums1_idx = 0
    nums2_idx = 0
    intersection = []
    while nums1_idx < len(nums1) and nums2_idx < len(nums2):
        if nums1[nums1_idx] == nums2[nums2_idx]:
            intersection.append(nums1[nums1_idx])
            nums1_idx += 1
            nums2_idx += 1
        elif nums1[nums1_idx] > nums2[nums2_idx]:
            nums2_idx += 1
        else:
            nums1_idx += 1

    return intersection



# Tests
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(array_intersection(nums1, nums2))

nums1 = [2, 2]
nums2 = [1, 2, 2, 1]
print(array_intersection(nums1, nums2))

nums1 = []
nums2 = []
print(array_intersection(nums1, nums2))

nums1 = range(1000, 1, -1)
nums2 = range(1, 1000, 33)
print(array_intersection(nums1, nums2))

import random
nums1 = [random.randint(0, 5000) for _ in range(1000 // 2)]
nums2 = [random.randint(0, 5000) for _ in range(1000 // 3)]
print(array_intersection(nums1, nums2))

# Time complexity
from timeit import Timer

print()
print('Ordered test lists')
nums1 = list(range(1, 1000, 2))
nums2 = list(range(1, 1000, 3))

t1 = Timer('array_intersection(nums1, nums2)',
           'from __main__ import array_intersection, nums1, nums2')
print(' Time 3rd attempt 10x   {0:4f}'.format(t1.timeit(number = 10)))
print(' Time 3rd attempt 100x  {0:4f}'.format(t1.timeit(number = 100)))
print(' Time 3rd attempt 1000x {0:4f}'.format(t1.timeit(number = 1000)))

print()
t2 = Timer('array_intersection_secondattempt(nums1, nums2)',
           ('from __main__ import array_intersection_secondattempt,'
            'nums1, nums2'))
print(' Time 2nd attempt 10x   {0:4f}'.format(t2.timeit(number = 10)))
print(' Time 2nd attempt 100x  {0:4f}'.format(t2.timeit(number = 100)))
print(' Time 2nd attempt 1000x {0:4f}'.format(t2.timeit(number = 1000)))

print()
t2 = Timer('array_intersection_firstattempt(nums1, nums2)',
           ('from __main__ import array_intersection_fisrtattempt,'
            'nums1, nums2'))
print(' Time 1st attempt 10x   {0:4f}'.format(t1.timeit(number = 10)))
print(' Time 1st attempt 100x  {0:4f}'.format(t1.timeit(number = 100)))
print(' Time 1st attempt 1000x {0:4f}'.format(t1.timeit(number = 1000)))


print()
print('Random test lists')
import random
nums1 = [random.randint(0, 1000) for _ in range(1000 // 2)]
nums2 = [random.randint(0, 1000) for _ in range(1000 // 3)]

t1 = Timer('array_intersection(nums1, nums2)',
           'from __main__ import array_intersection, nums1, nums2')
print(' Time 3rd attempt 10x   {0:4f}'.format(t1.timeit(number = 10)))
print(' Time 3rd attempt 100x  {0:4f}'.format(t1.timeit(number = 100)))
print(' Time 3rd attempt 1000x {0:4f}'.format(t1.timeit(number = 1000)))

print()
t2 = Timer('array_intersection_secondattempt(nums1, nums2)',
           ('from __main__ import array_intersection_secondattempt,'
            'nums1, nums2'))
print(' Time 2nd attempt 10x   {0:4f}'.format(t2.timeit(number = 10)))
print(' Time 2nd attempt 100x  {0:4f}'.format(t2.timeit(number = 100)))
print(' Time 2nd attempt 1000x {0:4f}'.format(t2.timeit(number = 1000)))

print()
t2 = Timer('array_intersection_firstattempt(nums1, nums2)',
           ('from __main__ import array_intersection_fisrtattempt,'
            'nums1, nums2'))
print(' Time 1st attempt 10x   {0:4f}'.format(t1.timeit(number = 10)))
print(' Time 1st attempt 100x  {0:4f}'.format(t1.timeit(number = 100)))
print(' Time 1st attempt 1000x {0:4f}'.format(t1.timeit(number = 1000)))

