class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """

    def longestIncreasingSubsequence(self, nums):
        if not nums:
            return 0

        dp = [1] * len(nums)
        result = -sys.maxsize

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
            result = max(result, dp[i])

        return result