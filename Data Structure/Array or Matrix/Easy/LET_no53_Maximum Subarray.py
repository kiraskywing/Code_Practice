class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """

    def maxSubArray(self, nums):
        prefix_min, prefix_max = 0, -sys.maxsize
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            prefix_max = max(prefix_max, prefix_sum - prefix_min)
            prefix_min = min(prefix_sum, prefix_min)

        return prefix_max

class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum, res = 0, float('-inf')
        for num in nums:
            cur_sum = max(cur_sum + num, num)
            res = max(res, cur_sum)
        return res