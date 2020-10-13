import heapq

class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        self.size = k
        self.heap = []

    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        heapq.heappush(self.heap, num)
        if len(self.heap) > self.size:
            heapq.heappop(self.heap)

    """
    @return: Top k element
    """
    def topk(self):
        return sorted(self.heap, reverse=True)
