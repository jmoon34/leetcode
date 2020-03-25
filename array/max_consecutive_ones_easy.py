# Given a binary array, find the maximum number of consecutive 1s in this array.
#
# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.
# Note:
#
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000

# [0,1,1,0,0,1,1,1]
def consecutive_ones(nums):
    lens = [0 for _ in range(len(nums))]
    len_index = 0
    max_len = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            lens[len_index] += 1
            max_len = max(max_len, lens[len_index])
        else:
            len_index = i + 1
    return max_len

def consecutive_ones_fast(nums):
    return max(map(len, ''.join(map(str, nums)).split('0')))

# print(consecutive_ones([0,1,1,0,0,1,1,1]))
# print(consecutive_ones([0,1,1,0]))
x = [0,1,1,0,0,1,1,1]
y = list(map(str, x))
z = ''.join(y)
u = z.split('0')
v = list(map(len, u))
print(x)
print(y)
print(z)
print(u)
print(v)