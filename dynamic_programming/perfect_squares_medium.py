# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Example 1:
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
#
# Example 2:
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

def min_num_perfect_squares(n):
    import math
    if int(math.sqrt(n)) == math.sqrt(n): return 1
    squares = [i**2 for i in range(1, int(math.sqrt(n))+1)]
    print(squares, math.sqrt(n))
    min_nums = [float('inf')] * (n+1)
    min_nums[0] = 0
    for num in range(1, n+1):
        for square in squares:
            if num - square >= 0:
                min_nums[num] = min(min_nums[num], min_nums[num-square] + 1)
    return min_nums[-1]

print(min_num_perfect_squares(13))