class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        mod = 10 ** 9 + 7
        
        for i in range(1, n + 1):
            dp[i][0] = 1
            for j in range(1, k + 1):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
                if j >= i: 
                    dp[i][j] -= dp[i - 1][j - i]
                dp[i][j] %= mod
        
        return dp[n][k]