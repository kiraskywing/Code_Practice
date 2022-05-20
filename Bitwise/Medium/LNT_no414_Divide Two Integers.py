# The same as LeetCode no29. Divide Two Integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -(2 ** 31) and divisor == -1:
            return 2 ** 31 - 1
        
        a, b, res = abs(dividend), abs(divisor), 0
        for i in range(31, -1, -1):
            if a >= b << i:
                res += 1 << i
                a -= b << i
        return res if (dividend > 0) == (divisor > 0) else -res