class MyCircularQueue:

    def __init__(self, k: int):
        self.cur = 0
        self.size = k
        self.front = self.rear = -1
        self.queue = [0] * k

    def enQueue(self, value: int) -> bool:
        if self.cur == self.size: return False
        
        if self.rear == -1:
            self.rear = self.front = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.cur += 1
        self.queue[self.rear] = value
        
        return True

    def deQueue(self) -> bool:
        if self.cur == 0: return False
        
        if self.front == self.rear: 
            self.front = self.rear = -1
        else: 
            self.front = (self.front + 1) % self.size
        self.cur -= 1
        return True

    def Front(self) -> int:
        return self.queue[self.front] if self.cur > 0 else -1

    def Rear(self) -> int:
        return self.queue[self.rear] if self.cur > 0 else -1

    def isEmpty(self) -> bool:
        return self.cur == 0

    def isFull(self) -> bool:
        return self.cur == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()