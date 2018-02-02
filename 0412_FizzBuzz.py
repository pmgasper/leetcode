#!/usr/bin/env python3
#
# Write a program that outputs the string representation of numbers from 1 to n.
# But for multiples of three it should output “Fizz” instead of the number and 
# for the multiples of five output “Buzz”. For numbers which are multiples of 
# both three and five output “FizzBuzz”.


def fizzbuzz(n):
    ''' return a list of strings '''
    return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i)
            for i in range(1, n + 1 )]


def fizzbuzz_firstattempt(n):
    ''' return a list of strings '''
    str_list = []

    for idx in range(1, n + 1):
        num_str = ''
        if idx % 3 == 0:
            num_str += 'Fizz'
        if idx % 5 == 0:
            num_str += 'Buzz'
        if idx % 3 != 0 and idx % 5 != 0:
            num_str += str(idx)
        str_list.append(num_str)

    return str_list


# Tests
for string in fizzbuzz(15):
    print(string)
print()
print(fizzbuzz(0))
