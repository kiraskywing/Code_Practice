class MedianFinder:

    def __init__(self):
        self.first, self.second = [], []
        self.size = 0

    def addNum(self, num: int) -> None:
        self.size += 1
        if len(self.second) < len(self.first):
            heapq.heappush(self.second, num)
        else:
            heapq.heappush(self.first, -num)
            
        if self.second and -self.first[0] > self.second[0]:
            heapq.heappush(self.second, -heapq.heappop(self.first))
            heapq.heappush(self.first, -heapq.heappop(self.second))

    def findMedian(self) -> float:
        if self.size % 2 != 0:
            return -self.first[0]
        return (-self.first[0] + self.second[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()