class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        
        afterRest, afterBuy, afterSell = [0] * n, [0] * n, [0] * n
        afterRest[0] = 0
        afterBuy[0] = -prices[0]
        afterSell[0] = float('-inf')
        
        for i in range(1, n):
            afterRest[i] = max(afterRest[i - 1], afterSell[i - 1])
            afterBuy[i] = max(afterBuy[i - 1], afterRest[i - 1] - prices[i])
            afterSell[i] = afterBuy[i - 1] + prices[i]
        
        return max(afterRest[n - 1], afterSell[n - 1])