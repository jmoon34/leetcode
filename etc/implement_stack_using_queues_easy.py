from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = deque()
        self.s2 = deque()
        self.size = 0

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.s1.append(x)
        self.size += 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        for i in range(self.size-1):
            self.s1.append(self.s1.popleft())
        self.size -= 1
        return self.s1.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        for i in range(self.size-1):
            self.s1.append(self.s1.popleft())
        x = self.s1.popleft()
        self.s1.append(x)
        return x

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.s1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
