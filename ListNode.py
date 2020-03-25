class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

    def printer(self):
        current = self
        while current is not None:
            print(current.val, end="->")
            current = current.next
        print(None)

    def __str__(self):
        s = ""
        current = self
        while current is not None:
            s += str(current.val) + "->"
            current = current.next
        s += str(None)
        return s

    def __repr__(self):
        return str(self)

    @staticmethod
    def array_to_LL(arr):
        l = ListNode(arr[0])
        current = l
        for i in range(1, len(arr)):
            current.next = ListNode(arr[i])
            current = current.next
        return l


