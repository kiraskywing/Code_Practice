class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        square = [i ** 2 for i in range(1, int(n ** 0.5) + 1)]
        
        for i in range(n + 1):
            for num in square:
                if num > i:
                    break
                dp[i] = min(dp[i], dp[i - num] + 1)
        
        return dp[-1]
        