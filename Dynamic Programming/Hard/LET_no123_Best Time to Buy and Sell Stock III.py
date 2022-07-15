class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """

    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0

        hold1 = hold2 = float('-inf')
        release1 = release2 = 0
        for p in prices:
            release2 = max(release2, hold2 + p)
            hold2 = max(hold2, release1 - p)
            release1 = max(release1, hold1 + p)
            hold1 = max(hold1, -p)
        return release2

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * n for _ in range(2)]
        prev, cur = 1, 0
        
        for _ in range(2):
            prev, cur = cur, prev
            buy_price = -prices[0]
            for j in range(1, n):
                dp[cur][j] = max(dp[cur][j - 1], buy_price + prices[j])
                buy_price = max(buy_price, dp[prev][j - 1] - prices[j])
        
        return dp[cur][-1]
