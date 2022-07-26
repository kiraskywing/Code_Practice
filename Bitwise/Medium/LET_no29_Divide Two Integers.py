class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a, b = abs(dividend), abs(divisor)
        res = 0
        for i in range(31, -1, -1):
            if a >= b << i:
                res += 1 << i
                a -= b << i
        
        if not ((dividend > 0) == (divisor > 0)):
            res = -res
            
        if res < -(2 ** 31):
            return -(2 ** 31)
        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return res