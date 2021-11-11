class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        res, cur = 1, 0
        for num in nums:
            cur += num
            res = max(res, -cur + 1)
        return res 