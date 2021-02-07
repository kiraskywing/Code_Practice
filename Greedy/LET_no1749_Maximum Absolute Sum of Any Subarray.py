class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix_sum = [0] + list(accumulate(nums))
        return max(prefix_sum) - min(prefix_sum)