class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        if not triangle or not triangle[0]:
            return -1

        dp = [[0] * (i + 1) for i in range(len(triangle))]

        for i in range(len(triangle[-1])):
            dp[-1][i] = triangle[-1][i]

        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]

        return dp[0][0]
