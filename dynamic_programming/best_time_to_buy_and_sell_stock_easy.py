# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
# design an algorithm to find the maximum profit.
#
# Note that you cannot sell a stock before you buy one.
#
# Example 1:
#
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

# [7,6,4,3,1]
# [0,max(0, prices[1]-prices[0])]

# [7,1,5,3,6,4]
# [0,max(-6,0), max(0, p[2]-p[1])=4,
# [7,1,4,6,2,5,4,9]
# [0,0,3,5,5,5,5,

# Not really a dynamic programming problem.. i think it has a wrong tag
# O(n) time, O(n) space because I solved it like a dynamic programming problem
def trade_stock(prices):
        profit = prices[:]
        smallest = prices[0]
        profit[0] = 0
        for i in range(1, len(prices)):
            smallest = min(smallest, prices[i])
            if prices[i] > prices[i-1]:
                profit[i] = max(prices[i] - smallest, profit[i-1])
            else:
                profit[i] = profit[i-1]
        return max(profit)

# O(n) time O(1) space
def trade_stock_simpler(prices):
    min_price = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        if prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
    return max_profit

print(trade_stock_simpler([7,1,4,6,2,5,4,9,]))

