# For a sorted array, implement binary search

import random

def linear_search(arr, k):
    for i in range(len(arr)):
        if arr[i] == k:
            return i
    return -1


def binary_search(arr, k):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < k:
            left = mid + 1
        elif arr[mid] == k:
            return mid
        elif arr[mid] > k:
            right = mid - 1
    return -1


def stress_test(max_arr_size=10**3, max_num=10**4):
    while True:
        test_arr = []
        while len(test_arr) < max_arr_size:
            x = random.randint(-max_num, max_num)
            if x not in test_arr:
                test_arr.append(x)
        list.sort(test_arr)
        k = max_num + 1
        while k not in test_arr:
            k = random.randint(-max_num, max_num)
        linear = linear_search(test_arr, k)
        binary = binary_search(test_arr, k)
        if linear == binary:
            print("SUCCESS", k, test_arr)
        else:
            print("FAIL")
            print("linear:", linear, "binary:", binary)
            break



stress_test()

# Binary search to find the lower end of any duplicate elements
# e.g. x = [0,2,4,4,5,7,7,7,8]
# input: 4, output: 2
# input: 7, output 5
def binary_search_lower_end(arr, k):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    return left

# Binary search to find the lower end of any duplicate elements
# e.g. x = [0,2,4,4,5,7,7,7,8]
# input: 4, output: 3
# input: 7, output 7
def binary_search_upper_end(arr, k):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= k:
            left = mid + 1
        else:
            right = mid - 1
    return right

