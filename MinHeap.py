import sys
class MinHeap:
    def __init__(self):
        self.heap = []

    # O(log n) since it uses sift-down
    def pop_min(self):
        m = self.heap[0]
        self.heap[0], self.heap[len(self.heap)-1] = self.heap[len(self.heap)-1], self.heap[0]
        self.heap.pop(-1)
        self.sift_down(0)
        return m

    # O(1)
    def get_min(self):
        return self.heap[0]

    # O(log n), complete binary tree. let n' = num nodes after completing last level. n' < 2n
    # n' = 2^h -1
    # => h = log_2(n'-1) < log_2(2n+1), therefore O(log n) for all operations involving sift_up & sift_down
    def sift_up(self, i):
        while self.heap[(i-1)//2] > self.heap[i] and i > 0:
            self.heap[(i-1)//2], self.heap[i] = self.heap[i], self.heap[(i-1)//2]
            i = (i-1)//2

    def sift_down(self, i):
        while 2*i+2 < len(self.heap) and (self.heap[2*i+1] < self.heap[i] or self.heap[2*i+2] < self.heap[i]):
            if self.heap[2*i+1] <= self.heap[2*i+2]:
                self.heap[2*i+1], self.heap[i] = self.heap[i], self.heap[2*i+1]
                i = 2*i + 1
            else:
                self.heap[2*i+2], self.heap[i] = self.heap[i], self.heap[2*i+2]
                i = 2*i + 2
        if 2*i + 1 < len(self.heap):
            if self.heap[2*i+1] < self.heap[i]:
                self.heap[i], self.heap[2*i+1] = self.heap[2*i+1], self.heap[i]
                i = 2*i + 1


    # O(log n)
    def add(self, x):
        self.heap.append(x)
        self.sift_up(len(self.heap)-1)

    # O(log n)
    def remove(self, i):
        self.heap[i] = -sys.maxsize
        self.sift_up(i)
        self.pop_min()

    # O(log n)
    def change_priority(self, i, p):
        prev_p = self.heap[i]
        self.heap[i] = p
        if p < prev_p:
            self.sift_up(i)
        else:
            self.sift_down(i)




m = MinHeap()
m.heap = [0,4,2,5,7,6,8]
print(m.pop_min())
print(m.heap)