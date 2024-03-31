class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        min_i = max_i = bad_i = -1
        for i, num in enumerate(nums):
            if not minK <= num <= maxK:
                bad_i = i
            if num == minK:
                min_i = i
            if num == maxK:
                max_i = i
            res += max(0, min(min_i, max_i) - bad_i)
        
        return res