class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = cur = 0
        for i in nums:
            cur = cur + 1 if i else 0
            res = max(res, cur)
        return res