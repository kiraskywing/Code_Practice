class Solution:
    def countOrders(self, n: int) -> int:
        res, mod = 1, 10 ** 9 + 7
        for i in range(1, n + 1):
            res = res * (i * 2 - 1) * i % mod
        return res