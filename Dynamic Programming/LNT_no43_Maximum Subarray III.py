class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """

    def maxSubArray(self, nums, k):
        n = len(nums)

        # dp1 为取当前数的状态 dp2 为不取当前数的状态
        dp1 = [[-sys.maxsize for _ in range(k + 1)] for _ in range(n + 1)]
        dp2 = [[-sys.maxsize for _ in range(k + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            dp1[i][0] = 0
            dp2[i][0] = 0
            for j in range(1, min(i + 1, k + 1)):
                dp1[i][j] = max(dp1[i - 1][j] + nums[i - 1], dp1[i - 1][j - 1] + nums[i - 1],
                                dp2[i - 1][j - 1] + nums[i - 1])
                dp2[i][j] = max(dp1[i - 1][j], dp2[i - 1][j])

        return max(dp1[-1][-1], dp2[-1][-1])
