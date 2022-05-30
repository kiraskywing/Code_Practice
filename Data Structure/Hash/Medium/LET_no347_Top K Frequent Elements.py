class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        memo = collections.Counter(nums)
        n = len(nums)
        freqs = [[] for _ in range(n + 1)]
        for num, freq in memo.items():
            freqs[freq].append(num)
        
        res = []
        for f in range(n, 0, -1):
            if freqs[f]:
                res.extend(freqs[f])
                if len(res) >= k:
                    return res[:k]
        
        return res[:k]

class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        memo = collections.Counter(nums)
        h = []
        for val, freq in memo.items():
            heapq.heappush(h, (freq, val))
            if len(h) > k:
                heapq.heappop(h)
            
        return [val for freq, val in h]