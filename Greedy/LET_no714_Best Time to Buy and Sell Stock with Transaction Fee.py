class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) < 2:
            return 0
        
        res, minimum = 0, prices[0]
        for i in range(1, len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            elif prices[i] > minimum + fee:
                res += prices[i] - minimum - fee
                minimum = prices[i] - fee
        
        return res