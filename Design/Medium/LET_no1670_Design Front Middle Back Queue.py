class FrontMiddleBackQueue:

    def __init__(self):
        self.front_half, self.back_half = collections.deque(), collections.deque()

    def pushFront(self, val: int) -> None:
        self.front_half.appendleft(val)
        self.balance()

    def pushMiddle(self, val: int) -> None:
        if len(self.front_half) > len(self.back_half):
            self.back_half.appendleft(self.front_half.pop())
        self.front_half.append(val)

    def pushBack(self, val: int) -> None:
        self.back_half.append(val)
        self.balance()

    def popFront(self) -> int:
        val = self.front_half.popleft() if self.front_half else -1
        self.balance()
        return val

    def popMiddle(self) -> int:
        val = self.front_half.pop() if self.front_half else -1
        self.balance()
        return val

    def popBack(self) -> int:
        val = (self.back_half or self.front_half or [-1]).pop()
        self.balance()
        return val
        
    def balance(self):
        if len(self.front_half) > len(self.back_half) + 1:
            self.back_half.appendleft(self.front_half.pop())
        if len(self.front_half) < len(self.back_half):
            self.front_half.append(self.back_half.popleft())
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()