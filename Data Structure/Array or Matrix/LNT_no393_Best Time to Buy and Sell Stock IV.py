class Solution:
    """
    @param K: An integer
    @param prices: An integer array
    @return: Maximum profit
    """

    def maxProfit(self, K, prices):
        if len(prices) <= 1:
            return 0

        if K > len(prices) // 2:
            return self.max_gain(prices)

        max_price = max(prices)
        save = [-max_price for _ in range(K)]
        gain = [0 for _ in range(K)]

        for price in prices:
            for i in range(K):
                save[i] = max(save[i], -price if i == 0 else gain[i - 1] - price)
                gain[i] = max(gain[i], price + save[i])

        return gain[-1]

    def max_gain(self, prices):
        result = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                result += prices[i] - prices[i - 1]
        return result
