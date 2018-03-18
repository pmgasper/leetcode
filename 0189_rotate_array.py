#!/usr/bin/env python3
#
# Rotate an array of n elements to the right by k steps.
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to
# [5,6,7,1,2,3,4].
#
# Note: Try to come up as many solutions as you can, there are at least 3 
# different ways to solve this problem.


def rotate_array_slice(nums, k):
    # slice and concationate
    n = len(nums)
    nums[:] = nums[n - k:] + nums[:n - k]


def rotate_array_queue(nums, k):
    # queue
    from collections import deque
    queue = deque()
    k = k % len(nums)

    for idx, num in enumerate(nums):
        queue.append(num)
        if idx >= k:
            nums[idx] = queue.popleft()

    for idx in range(len(queue)):
        nums[idx] = queue.popleft()
    

def rotate_array_queue2(nums, k):
    # alternative queue use
    from collections import deque
    queue = deque(nums)
    k = k % len(nums)

    for _ in range(k):
        queue.appendleft(queue.pop())

    nums[:] = queue



# Tests
nums = [1, 2, 3, 4, 5, 6, 7]
rotate_array_queue2(nums, 3)
print(nums)
    
nums = [1, 2, 3, 4, 5, 6, 7]
rotate_array_queue2(nums, 5)
print(nums)

nums = [1, 2]
rotate_array_queue(nums, 3)
print(nums)



