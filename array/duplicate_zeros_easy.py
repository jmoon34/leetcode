# Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
#
# Note that elements beyond the length of the original array are not written.
#
# Do the above modifications to the input array in place, do not return anything from your function.
#
# Example 1:
#
# Input: [1,0,2,3,0,4,5,0]
# Output: null
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
# Example 2:
#
# Input: [1,2,3]
# Output: null
# Explanation: After calling your function, the input array is modified to: [1,2,3]
#
#
# Note:
#
# 1 <= arr.length <= 10000
# 0 <= arr[i] <= 9

# [1,0,2,3,0,4,5,0]
# [1,0,0,2,3,0,4,5]
# [1,0,0,2,3,0,0,4]
def duplicate_zeros_slow(arr):
    i = 0
    while i < len(arr) - 1:
        if arr[i] == 0:
            for j in range(-1, -len(arr)+i+1, -1):
                arr[j] = arr[j-1]
            arr[i+1] = 0
            i += 1
        i += 1

# [3,2,0,0,0,0,7]
# [3,2,0,o,0,0,7]
# [3,2,0,o,0,o,0]

# [3,2,0,0,0,7]
# [3,2,0,o,0,0]
# [3,2,0,o,0,o]
def duplicate_zeros_fast(arr):
    num_dupes = 0
    last_index = len(arr) - 1
    for i in range(len(arr)):
        if i > last_index - num_dupes:
            break
        if arr[i] == 0:
            if i == last_index - num_dupes:
                arr[last_index] = 0
                last_index -= 1
                break
            num_dupes += 1

    last = last_index - num_dupes

    # Copy zero twice, and non zero once.
    for i in range(last, -1, -1):
        if arr[i] == 0:
            arr[i + num_dupes] = 0
            num_dupes -= 1
            arr[i + num_dupes] = 0
        else:
            arr[i + num_dupes] = arr[i]






a = [1,0,2,3,0,4,5,0]
duplicate_zeros_fast(a)
print(a)



