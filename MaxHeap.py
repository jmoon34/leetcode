


class MaxHeap:

    def __init__(self, n=0):
        self.heap = []
        self.n = 0

    def sift_down(self, i):
        # both children exist
        while 2*i + 2 < self.n and (self.heap[i] < self.heap[2*i+1] or self.heap[i] < self.heap[2*i+2]):
            if self.heap[2*i+1] > self.heap[2*i+2]:
                self.heap[i], self.heap[2*i+1] = self.heap[2*i+1], self.heap[i]
                i = 2*i + 1
            else:
                self.heap[i], self.heap[2*i+2] = self.heap[2*i+2], self.heap[i]
                i = 2*i + 2
        # edge case: last level and only left child exists
        if 2*i + 1 < self.n:
            if self.heap[2*i+1] > self.heap[i]:
                self.heap[i], self.heap[2*i+1] = self.heap[2*i+1], self.heap[i]
                i = 2*i + 1

    def sift_up(self, i):
        while i > 0 and self.heap[(i-1)//2] < self.heap[i]:
            self.heap[i], self.heap[(i-1)//2] = self.heap[(i-1)//2], self.heap[i]
            i = (i-1) // 2

    def add(self, i):
        self.heap.append(i)
        self.n += 1
        self.sift_up(self.n - 1)

    def pop_max(self):
        m = self.heap[0]
        self.heap[0], self.heap[self.n-1] = self.heap[self.n-1], self.heap[0]
        self.heap.pop()
        self.n -= 1
        self.sift_down(0)
        return m

    def remove(self, i):
        self.heap[i] = float('inf')
        self.sift_up(i)
        self.pop_max()
        self.n -= 1


    def change_priority(self, i, p):
        prev_p = self.heap[i]
        self.heap[i] = p
        if prev_p < p:
            self.sift_up(i)
        else:
            self.sift_down(i)

    # heapify using sift_up.  More nodes near the bottom so this works in O(nlogn) time
    @staticmethod
    def heapify_slow(arr):
        m = MaxHeap()
        m.heap = arr
        m.n = len(arr)
        for i in range(1, m.n):
            m.sift_up(i)
        return arr

    # heapify using sift_down.  Less nodes near the top so this works in O(n) time
    @staticmethod
    def heapifly_fast(arr):
        m = MaxHeap()
        m.heap = arr
        m.n = len(arr)
        for i in range(m.n-1)[::-1]:
            m.sift_down(i)
        return arr

    @staticmethod
    def heap_sort(arr):
        m = MaxHeap()
        m.heap = arr[:]
        m.n = len(arr)
        for i in range(m.n-1)[::-1]:
            m.sift_down(i)
        for i in range(m.n)[::-1]:
            print(i, arr, arr[i])
            arr[i] = m.pop_max()
        return arr


a = [9,4,2,8,5,1,2]
print(MaxHeap.heapify_slow(a))
print(MaxHeap.heapifly_fast(a))
print(MaxHeap.heap_sort(a))