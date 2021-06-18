class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        res, dp, prev = 0, 0, -1
        for i, num in enumerate(nums):
            if num > right:
                dp = 0
                prev = i
            elif num >= left:
                dp = i - prev
            res += dp
        return res