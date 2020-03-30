# You are given coins of different denominations and a total amount of money amount.
# Write a function to compute the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.
#
# Example 1:
#
# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:
#
# Input: coins = [2], amount = 3
# Output: -1
# Note:
# You may assume that you have an infinite number of each kind of coin.


# [1,2,5]  11
# [0,1,2,3,4,5,6,7,8,9,10,11]
# [0,1,1,2,2,

# In this method, I wasn't aware you could do something like float('inf') and I was too lazy to use sys.maxsize
# So I used amount+1 as a large number that will be changed.  Even if 1 in coins, maximum will min number of coins
# for amount will equal to amount, so I just added 1, making it unreachable no matter what the input.
def coin_change(coins, amount):
    min_num = [0 for _ in range(amount+1)]
    for n in range(1, len(min_num)):
        min_num[n] = amount+1
        for coin in coins:
            if n - coin >= 0:
                min_num[n] = min(min_num[n], min_num[n-coin] + 1)
    return min_num[amount] if min_num[amount] != amount+1 else -1

print(coin_change([2], 1))
[].ins