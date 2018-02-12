#!/usr/bin/env python3
#
# Say you have an array for which the ith element is the price of a given stock
# on day i. If you were only permitted to complete at most one transaction 
# (ie, buy one and sell one share of the stock), design an algorithm to find 
# the maximum profit.


def max_profit(prices):

    max_profit = 0
    if prices:
        low = prices[0]

    for price in prices[1:]:
        low = min(low, price)
        max_profit = max(max_profit, price - low)

    return max_profit


def max_profit_firstattempt(prices):

    max_profit = 0

    if prices:
        low = prices[0]

    for price in prices[1:]:
        if price > low:
            potential_profit = price - low
            if potential_profit > max_profit:
                max_profit = potential_profit
        else:
            low = price

    return max_profit


# Tests
print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([1]))
print(max_profit([]))
print(max_profit([1, 7, 1, 5, 3, 6, 4]))
print(max_profit([1, 6, 1, 5, 3, 7, 4]))


