#!/usr/bin/env python3
#
# Given four lists A, B, C, D of integer values, compute how many 
# tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
#
# To make problem a bit easier, all A, B, C, D have same length of N 
# where 0 ≤ N ≤ 500. All integers are in the range of -2**28 to 2**28 - 1 and 
# the result is guaranteed to be at most 2**31 - 1. 


def four_sum_count(a, b, c, d):
    # Works, but inefficient 
    ab = [a_i + b_j for a_i in a for b_j in b]
    cd = [c_i + d_j for c_i in c for d_j in d]

    return len([1 for ab_i in ab for cd_j in cd if ab_i == -cd_j])


def four_sum_count2(a, b, c, d):
    # Store count to reduce number of comparisons
    from collections import Counter
    ab = Counter([(a_i + b_j) for a_i in a for b_j in b])
    return sum([ab[-(c_i + d_j)] for c_i in c for d_j in d])
    

# Tests
a = [ 1, 2]
b = [-2,-1]
c = [-1, 2]
d = [ 0, 2]
print(four_sum_count2(a, b, c, d))   # 2

a = [0] * 100
b = [0] * 100
c = [0] * 100
d = [0] * 100
print(four_sum_count2(a, b, c, d))   # 100000000 (100**4)


# Timing
from timeit import Timer
a = [0] * 10
b = [0] * 10
c = [0] * 10
d = [0] * 10

t1 = Timer('four_sum_count(a, b, c, d)',
           'from __main__ import four_sum_count, a, b, c, d')
print('four_sum_count  {0:.4f}'.format(t1.timeit(number = 1000)))

t1 = Timer('four_sum_count2(a, b, c, d)',
           'from __main__ import four_sum_count2, a, b, c, d')
print('four_sum_count2 {0:.4f}'.format(t1.timeit(number = 1000)))

