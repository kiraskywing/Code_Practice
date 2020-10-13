class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """

    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0

        save1, save2 = -max(prices), -max(prices)
        gain1, gain2 = 0, 0
        for price in prices:
            save1 = max(save1, -price)
            gain1 = max(gain1, price + save1)
            save2 = max(save2, gain1 - price)
            gain2 = max(gain2, price + save2)

        return gain2
