#!/usr/bin/env python3
#
# Say you have an array for which the ith element is the price of a given stock
# on day i. Design an algorithm to find the maximum profit. You may complete
# as many transactions as you like (ie, buy one and sell one share of the 
# stock multiple times). However, you may not engage in multiple
# transactions at the same time (ie, you must sell the stock before you buy
# again).

def max_profit(prices):
    # if price goes up assume we had stock - profit
    # if price goes down assume we didn't have stock - no loss 
    profit = 0
    for idx in range(1, len(prices)):
        if prices[idx] > prices[idx - 1]:
            profit += prices[idx] - prices[idx - 1]
    return profit


# Tests
print(max_profit([1,0,1,0,1]))
print(max_profit([1,1,1,1,1]))
print(max_profit([0,1,0,1,0]))
print(max_profit([0,2,0,4,0]))
