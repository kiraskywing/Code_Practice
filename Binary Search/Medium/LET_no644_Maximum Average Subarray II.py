class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        min_val, max_val = min(nums), max(nums)
        while min_val + 1e-5 <= max_val:
            mid = (min_val + max_val) / 2
            if self.is_valid(nums, mid, k):
                min_val = mid
            else:
                max_val = mid

        return max_val if self.is_valid(nums, max_val, k) else min_val

    def is_valid(self, nums, avg, k):
        cur = sum(nums[:k - 1]) - avg * (k - 1)
        pre = pre_min = 0
        
        for i in range(k - 1, len(nums)):
            cur += nums[i] - avg
            if cur - pre_min >= 0:
                return True
            
            pre += nums[i - k + 1] - avg
            pre_min = min(pre_min, pre)
        
        return False