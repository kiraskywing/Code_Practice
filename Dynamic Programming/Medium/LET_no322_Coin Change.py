class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        
        for i in range(1, amount + 1):
            dp[i] = min(dp[i - c] + 1 if i >= c else float('inf') for c in coins)
        
        return dp[-1] if dp[-1] != float('inf') else -1