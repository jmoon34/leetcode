def no_repeat(target, arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        print(left, right, mid)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
    return left



def highest_index(target, arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        print(left, right, mid)
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return right
# [1, 2, 2, 3, 3, 3, 4, 5, 5]

def lowest_index(target, arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        print(left, right, mid)
        if arr[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    return left

print(lowest_index(5, [1, 2, 2, 3, 3, 3, 4, 5, 5]))