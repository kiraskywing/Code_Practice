class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        low, high, n = min(nums), max(nums), len(nums)
        if n <= 2 or low == high:
            return high - low
        
        bucket = collections.defaultdict(list)
        for num in nums:
            index = n - 2 if num == high else (num - low) * (n - 1) // (high - low)
            bucket[index].append(num)
        
        candidates = [[min(bucket[i]), max(bucket[i])] for i in range(n - 1) if bucket[i]]
        return max(y[0] - x[1] for x, y in zip(candidates, candidates[1:]))