class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        res = float('inf')
        for right in range(len(nums)):
            target -= nums[right]
            while left <= right and target <= 0:
                res = min(res, right - left + 1)
                target += nums[left]
                left += 1
            
        return res if res != float('inf') else 0
                