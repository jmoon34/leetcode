# You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
#
# Given n, find the total number of full staircase rows that can be formed.
#
# n is a non-negative integer and fits within the range of a 32-bit signed integer.
#
# Example 1:
#
# n = 5
#
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤
#
# Because the 3rd row is incomplete, we return 2.
# Example 2:
#
# n = 8
#
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
#
# Because the 4th row is incomplete, we return 3.

# sum of first n numbers is n(n+1)/2
# [0, 1, 3, 6, 10, ...]
# if n = cum_sum[i] return i
# if n < cum_sum[i] return i-1
def arranged_coins(n):
    cum_sum = [0]
    for i in range(n+1):
        cum_sum.append(cum_sum[i] + i + 1)
        print(i, cum_sum)
        if n == cum_sum[i]:
            return i
        elif n < cum_sum[i]:
            return i-1


def arranged_coins_2(n):
    level = 0
    coins = 1
    while n >= coins:
        n -= coins
        coins += 1
        level += 1
    return level

def arranged_coins_math(n):
        import math
        return (-1 + math.sqrt(8*n + 1))//2


print(5//2)
print(arranged_coins_2(10))
