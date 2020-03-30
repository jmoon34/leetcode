# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
#
# Example:
# Given nums = [-2, 0, 3, -5, 2, -1]
#
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# Note:
# You may assume that the array does not change.
# There are many calls to sumRange function.

# [-2, -2, 1, -4, -2, -3]
# n[2]+n[3]+n[4]+n[5] = n[0]+n[1]+...+n[5] - (n[0]+n[1])
# => s(2,5) = s(0,5) - s(0,1)
# => s(a,b) = cum_sum[b] - cum_sum[a-1]
class NumArray:

    def __init__(self, nums):
        self.cum_sum = nums
        for i in range(1, len(nums)):
            self.cum_sum[i] += self.cum_sum[i-1]
    def sumRange(self, i, j):
        if i == 0:
            return self.cum_sum[j]
        else:
            return self.cum_sum[j] - self.cum_sum[i-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

o = NumArray([-2,0,3,-5,2,-1])
print(o.cum_sum)
p_1 = o.sumRange(0,2)
print(p_1)