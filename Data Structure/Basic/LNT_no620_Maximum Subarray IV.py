class Solution:
    """
    @param nums: an array of integer
    @param k: an integer
    @return: the largest sum
    """

    def maxSubarray4(self, nums, k):
        n = len(nums)
        if n < k:
            return 0

        pre_sum = [0 for _ in range(n + 1)]

        min_prefix, result = 0, -sys.maxsize
        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]
            if i >= k:
                result = max(pre_sum[i] - min_prefix, result)
                min_prefix = min(min_prefix, pre_sum[i - k + 1])
        return result
