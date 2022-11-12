class MedianFinder:

    def __init__(self):
        self.first, self.second = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.second, -heapq.heappushpop(self.first, -num))
        if len(self.second) > len(self.first):
            heapq.heappush(self.first, -heapq.heappop(self.second))

    def findMedian(self) -> float:
        return -self.first[0] if len(self.first) > len(self.second) else (-self.first[0] + self.second[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()