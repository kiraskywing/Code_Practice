# The same as LeetCode no295. Find Median from Data Stream
class MedianFinder:

    def __init__(self):
        self.first_half = []
        self.second_half = []

    def addNum(self, num: int) -> None:
        if not self.first_half or -self.first_half[0] >= num:
            heapq.heappush(self.first_half, -num)
        else:
            heapq.heappush(self.second_half, num)
        self.balance()
    
    def balance(self):
        if len(self.first_half) > len(self.second_half) + 1:
            val = heapq.heappop(self.first_half)
            heapq.heappush(self.second_half, -val)
        elif len(self.second_half) > len(self.first_half):
            val = heapq.heappop(self.second_half)
            heapq.heappush(self.first_half, -val)

    def findMedian(self) -> float:
        if (len(self.first_half) + len(self.second_half)) % 2:
            return -self.first_half[0]
        return (-self.first_half[0] + self.second_half[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()