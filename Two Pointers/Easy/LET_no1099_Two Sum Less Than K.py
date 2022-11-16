class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        res = float('-inf')
        
        while left < right:
            cur = nums[left] + nums[right]
            if cur < k:
                res = max(res, cur)
                left += 1
            else:
                right -= 1
        
        return res if res != float('-inf') else -1