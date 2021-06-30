class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = res = 0
        for right in range(len(nums)):
            k -= 1 - nums[right]
            while k < 0:
                k += 1 - nums[left]
                left += 1
            res = max(res, right - left + 1)
        
        return res