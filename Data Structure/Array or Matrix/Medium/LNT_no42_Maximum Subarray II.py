class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """

    def maxTwoSubArrays(self, nums):
        left_max, right_max = [0] * len(nums), [0] * len(nums)
        self.get_max_sum(left_max, nums)
        self.get_max_sum(right_max, nums[::-1])
        right_max = right_max[::-1]

        result = -sys.maxsize
        for i in range(len(nums) - 1):
            result = max(result, left_max[i] + right_max[i + 1])
        return result

    def get_max_sum(self, max_sum, nums):
        prefix = 0
        pre_min, pre_max = 0, -sys.maxsize
        for i in range(len(nums)):
            prefix += nums[i]
            pre_max = max(pre_max, prefix - pre_min)
            pre_min = min(pre_min, prefix)
            max_sum[i] = pre_max