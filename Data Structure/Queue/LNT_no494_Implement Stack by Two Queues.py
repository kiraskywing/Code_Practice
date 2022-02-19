# The same as LeetCode no225. Implement Stack using Queues

from queue import Queue

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que_main = Queue()
        self.que_sub = Queue()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.que_main.put(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while self.que_main.qsize() > 1:
            self.que_sub.put(self.que_main.get())

        val = self.que_main.get()

        self.que_main, self.que_sub = self.que_sub, self.que_main

        return val

    def top(self) -> int:
        """
        Get the top element.
        """
        while self.que_main.qsize() > 1:
            self.que_sub.put(self.que_main.get())

        val = self.que_main.get()

        self.que_main, self.que_sub = self.que_sub, self.que_main
        self.que_main.put(val)

        return val

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """

        return self.que_main.empty()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()