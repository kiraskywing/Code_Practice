class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        if not triangle or not triangle[0]:
            return -1

        dp = [[0] * (i + 1) for i in range(len(triangle))]
        dp[0][0] = triangle[0][0]

        for i in range(1, len(triangle)):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]

        for i in range(1, len(triangle)):
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]

        return min(dp[-1][i] for i in range(len(triangle[-1])))
