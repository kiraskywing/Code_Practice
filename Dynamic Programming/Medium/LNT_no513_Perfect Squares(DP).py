class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """

    def numSquares(self, n):
        dp = [sys.maxsize] * (n + 1)

        i = 0
        while i * i <= n:
            dp[i * i] = 1
            i += 1

        for i in range(n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1

        return dp[n]
