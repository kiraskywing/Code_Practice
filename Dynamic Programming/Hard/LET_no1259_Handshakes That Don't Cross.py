class Solution:
    def numberOfWays(self, num_people: int) -> int:

        mod = 10 ** 9 + 7
        pairs = num_people // 2
        # dp[n] 表示有n對握手
        # dp[n + 1] = dp[0] * dp[n] + dp[1] * dp[n - 1] + ... + dp[n] * dp[0]
        dp = [1] + [0] * pairs
        for i in range(1, pairs + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1] % mod

        return dp[pairs] % mod