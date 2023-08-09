class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left + 1 < right:
            mid = (left + right) // 2
            count = self.helper(nums, mid)
            if count >= p:
                right = mid
            else:
                left = mid

        return left if self.helper(nums, left) >= p else right
    
    def helper(self, nums, target):
        res = 0
        i = 1
        while i < len(nums):
            if nums[i] - nums[i - 1] <= target:
                res += 1
                i += 1
            i += 1
        
        return res