# the same as LeetCode no.151 Best Time to Buy and Sell Stock III

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
