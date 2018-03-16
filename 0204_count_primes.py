#!/usr/bin/env python3
#
# Count the number of prime numbers less than a non-negative number, n.

def count_primes_list(n):
    # second attempt keep list of non-primes

    if n < 2:
        return 0

    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    for i in range(2, n // 2 + 1):
        is_prime[i ** 2: n: i] = [False] * len(is_prime[i ** 2: n: i])

    return sum(is_prime)


def count_primes_set(n):
    # first attempt - keep set of non-primes

    prime_count = 0
    non_primes = set()
    for i in range(2, n):
        if i not in non_primes:
            prime_count += 1
            non_primes.update(range(i, n, i)[1:])

    return prime_count


# Tests
#print(count_primes(0))
#print(count_primes(1))
#print(count_primes(2))
#print(count_primes(5))
#print(count_primes(6561))


# Timing

from timeit import Timer

n = 12
print('n = ', n)

t1 = Timer('count_primes_list(n)', 
           'from __main__ import count_primes_list, n')
print('  list {0:.2f}'.format(t1.timeit(number=100000)))

t1 = Timer('count_primes_set(n)', 
           'from __main__ import count_primes_set, n')
print('  set  {0:.2f}'.format(t1.timeit(number=100000)))

print()

n = 12345
print('n = ', n)


t1 = Timer('count_primes_list(n)', 
           'from __main__ import count_primes_list, n')
print('  list {0:.2f}'.format(t1.timeit(number=100)))

t1 = Timer('count_primes_set(n)', 
           'from __main__ import count_primes_set, n')
print('  set  {0:.2f}'.format(t1.timeit(number=100)))


