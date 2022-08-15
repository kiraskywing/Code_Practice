class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        max_profit = 0
        buy_price = sys.maxsize
        for i in prices:
            buy_price = min(buy_price, i)
            max_profit = max(max_profit, i - buy_price)
        return max_profit
