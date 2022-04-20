class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        max_val, min_val = max(nums), min(nums)
        if n < 2 or max_val == min_val:
            return 0
        
        gap = int(math.ceil((max_val - min_val) / (n - 1)))
        bucket_size = int(math.ceil((max_val - min_val) / gap))
        b_mins = [float('inf')] * bucket_size
        b_maxs = [float('-inf')] * bucket_size
        
        for num in nums:
            if num == min_val or num == max_val:
                continue
            idx = (num - min_val) // gap
            b_mins[idx] = min(b_mins[idx], num)
            b_maxs[idx] = max(b_maxs[idx], num)
        
        res, prev = 0, min_val
        for i in range(bucket_size):
            if b_mins[i] == float('inf'):
                continue
            res = max(res, b_mins[i] - prev)
            prev = b_maxs[i]
        res = max(res, max_val - prev)
        return res
        