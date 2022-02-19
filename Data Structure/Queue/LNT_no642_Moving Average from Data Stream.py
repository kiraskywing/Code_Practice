# The same as LeetCode no346. Moving Average from Data Stream

class MovingAverage:
    """
    @param: size: An integer
    """

    def __init__(self, size):
        self.queue = collections.deque([])
        self.size = size
        self.result = 0

    """
    @param: val: An integer
    @return:  
    """

    def next(self, val):
        if len(self.queue) == self.size:
            self.result -= self.queue.popleft()

        self.result += val
        self.queue.append(val)

        return self.result / len(self.queue)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)