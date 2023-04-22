class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        for i in range(n):
            for j in range(n):
                if s[i] == s[-1 - j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        return n - dp[n][n]