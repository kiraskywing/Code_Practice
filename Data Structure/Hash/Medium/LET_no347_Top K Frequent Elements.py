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
        n = len(nums)
        memo = collections.Counter(nums)
        num_freq_pairs = [(num, freq) for num, freq in memo.items()]
        self.quickSelect(num_freq_pairs, 0, len(num_freq_pairs) - 1, k - 1)
        return [num for num, _ in num_freq_pairs[:k]]
    
    def quickSelect(self, pairs, left, right, target):
        if left >= right:
            return
        
        i, j = left, right
        pivot = pairs[random.randint(i, j)][1]
        while i <= j:
            while i <= j and pairs[i][1] > pivot:
                i += 1
            while i <= j and pairs[j][1] < pivot:
                j -= 1
            if i <= j:
                pairs[i], pairs[j] = pairs[j], pairs[i]
                i += 1
                j -= 1
                
        if target <= j:
            self.quickSelect(pairs, left, j, target)
        elif i <= target:
            self.quickSelect(pairs, i, right, target)

class Solution3:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        memo = collections.Counter(nums)
        h = []
        for val, freq in memo.items():
            heapq.heappush(h, (freq, val))
            if len(h) > k:
                heapq.heappop(h)
            
        return [val for freq, val in h]