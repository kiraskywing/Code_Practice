class Solution:
    def reverse(self, x: int) -> int:
        neg = x < 0
        x = abs(x)

        res = 0
        while x > 0:
            res = res * 10 + x % 10
            x //= 10

        res = -res if neg else res
        
        return res if (-(2 ** 31) <= res <= 2 ** 31 - 1) else 0