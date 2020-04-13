import random




def quick_sort(arr):
    def sort(arr, left, right):
        # print("left:", left, "right:", right)
        if left < right:
            m1, m2 = partition(arr, left, right)
            sort(arr, left, m1-1)
            sort(arr, m2+1, right)

    def partition(arr, left, right):
        p = random.randint(left, right)
        x = arr[p]
        arr[left], arr[p] = arr[p], arr[left]
        m1, m2 = left, left
        for i in range(left+1, right+1):
            if arr[i] < x:
                arr[m2+1], arr[i] = arr[i], arr[m2+1]
                arr[m1], arr[m2+1] = arr[m2+1], arr[m1]
                m1 += 1
                m2 += 1
            elif arr[i] == x:
                arr[m2+1], arr[i] = arr[i], arr[m2+1]
                m2 += 1
        # print("p:", p, "x:", x, "m1:", m1, "m2:", m2, "arr:", arr)
        return m1, m2
    sort(arr, 0, len(arr)-1)
    return arr

def bubble_sort(arr):
    for i in range(len(arr)-1):
        min_num = arr[i]
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < min_num:
                min_num = arr[j]
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def stress_test(max_len=10**3, max_n=10**4):
    while True:
        t1 = [random.randint(-max_n, max_n) for _ in range(max_len)]
        t2 = t1[:]
        bubble = bubble_sort(t1)
        quick = quick_sort(t2)
        if bubble == quick:
            print("SUCCESS")
        else:
            print("FAIL")
            print("bubble:", bubble)
            print("quick:", quick)
            break



# 1,3,2,4,2,5,6,8  ; p=4, arr[p] = 2 (second 2)
# 2,3,2,4,1,5,6,8

a = [1,3,2,4,2,5,6,8]
stress_test()