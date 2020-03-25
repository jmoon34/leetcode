# Given an array arr of integers, check if there exists two integers N and M such that N is the double of M
# ( i.e. N = 2 * M).
#
# More formally check if there exists two indices i and j such that :
#
# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]

# Input: arr = [10,2,5,3]
# Output: true
#
# Input: arr = [7,1,14,11]
# Output: true
#
# Input: arr = [3,1,7,11]
# Output: false

def check_double(arr):
    c = set()
    for i in range(len(arr)):
        num = arr[i]
        if num in c:
            return True
        if num % 2 == 0:
            c.add(num // 2)
        c.add(num * 2)
    return False

print(check_double([3,1,7,11]))




