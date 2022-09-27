class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = [0 for _ in range(k)]
        self.head = self.tail = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.isEmpty():
            self.head = self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.size
        
        self.queue[self.tail] = value
        
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.head == self.tail:
            self.head = self.tail = -1
        else:
            self.head = (self.head + 1 + self.size) % self.size
        
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.head == -1

    def isFull(self) -> bool:
        if self.head == self.tail == -1:
            return False
        return (self.tail + self.size - self.head + 1) % self.size == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()