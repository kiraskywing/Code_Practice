class Solution:
    def numTilings(self, n: int) -> int:
        a, b, c, d, mod = 0, 1, 1, 0, 10 ** 9 + 7
        n -= 1
        while n:
            d = (c * 2 % mod + a) % mod
            a = b
            b = c
            c = d
            n -= 1
        return c