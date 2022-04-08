class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.temp = []
        self.size = k
        for i in nums:
            heapq.heappush(self.temp, i)
        while len(self.temp) > self.size:
            heapq.heappop(self.temp)

    def add(self, val: int) -> int:
        heapq.heappush(self.temp, val)
        if len(self.temp) > self.size:
                heapq.heappop(self.temp)
        return self.temp[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)