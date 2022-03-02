class Solution:
    def twoEggDrop(self, n: int) -> int:
        dp = [0] * (n + 1)
        return self.helper(dp, n)
    
    def helper(self, dp, n):
        if dp[n] == 0:
            dp[n] = n
            for i in range(1, n + 1):
                dp[n] = min(dp[n], 1 + max(i - 1, self.helper(dp, n - i)))
        return dp[n]