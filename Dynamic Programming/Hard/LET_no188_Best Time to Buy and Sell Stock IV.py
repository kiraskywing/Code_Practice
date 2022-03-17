class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if k >= n // 2: return self.quickSolve(prices)
        
        dp = [[0] * n for _ in range(k + 1)]
        for i in range(1, k + 1):
            tmpMax = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], tmpMax + prices[j])
                tmpMax = max(tmpMax, dp[i - 1][j - 1] - prices[j])
        
        return dp[-1][-1]
    
    def quickSolve(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0: profit += prices[i] - prices[i - 1]
        return profit