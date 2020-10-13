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