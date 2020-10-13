class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two substrings
    """

    def maxDiffSubArrays(self, nums):
        if not nums:
            return 0

        n = len(nums)
        left_max, left_min = [0] * n, [0] * n
        right_max, right_min = [0] * n, [0] * n

        self.get_prefix_sum(left_max, left_min, nums)
        self.get_prefix_sum(right_max, right_min, nums[::-1])
        right_max, right_min = right_max[::-1], right_min[::-1]

        result = 0
        for i in range(n - 1):
            result = max(result, abs(left_max[i] - right_min[i + 1]), abs(left_min[i] - right_max[i + 1]))

        return result

    def get_prefix_sum(self, pre_max, pre_min, nums):

        prefix = 0
        min_sum_Max, max_sum_Max = 0, -sys.maxsize
        min_sum_Min, max_sum_Min = sys.maxsize, 0

        for i in range(len(nums)):
            prefix += nums[i]

            max_sum_Max = max(max_sum_Max, prefix - min_sum_Max)
            min_sum_Max = min(min_sum_Max, prefix)
            pre_max[i] = max_sum_Max

            min_sum_Min = min(min_sum_Min, prefix - max_sum_Min)
            max_sum_Min = max(max_sum_Min, prefix)
            pre_min[i] = min_sum_Min
