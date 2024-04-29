class Solution:
    def subsequenceSumOr(self, nums: List[int]) -> int:
        res = prefix = 0
        for num in nums:
            prefix += num
            res |= prefix | num

        return res