class Solution:
    def reverse(self, x: int) -> int:
        neg = x < 0
        res = 0
        x = abs(x)
        while x > 0:
            res = res * 10 + x % 10
            x //= 10
        
        if not (-(2 ** 31) <= res <= (2 ** 31 - 1)):
            return 0
        
        return res if not neg else -res