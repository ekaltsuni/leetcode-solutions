# 121. Best time to Buy and Sell
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and
# choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

from typing import List


def maxProfit(prices: List[int]) -> int:
    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)

    return max_profit

# Test Cases
prices = [7, 1, 5, 3, 6, 4]
result = maxProfit(prices)
print(result)

prices = [7, 6, 4, 3, 1]
result = maxProfit(prices)
print(result)

prices = [1, 2]
result = maxProfit(prices)
print(result)

prices = [2, 4, 1]
result = maxProfit(prices)
print(result)
