class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        memo = collections.Counter(nums)
        h = []
        for val, freq in memo.items():
            heapq.heappush(h, (freq, val))
            if len(h) > k:
                heapq.heappop(h)
            
        return [val for freq, val in h]