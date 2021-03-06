# The same as LeetCode no295. Find Median from Data Stream
import heapq

class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """

    def medianII(self, nums):
        self.minheap, self.maxheap = [], []
        result = []
        for num in nums:
            self.add(num)
            result.append(self.median)
        return result

    @property
    def median(self):
        return -self.maxheap[0]

    def add(self, value):
        if len(self.maxheap) <= len(self.minheap):
            heapq.heappush(self.maxheap, -value)
        else:
            heapq.heappush(self.minheap, value)

        if len(self.minheap) == 0 or len(self.maxheap) == 0:
            return

        if -self.maxheap[0] > self.minheap[0]:
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))