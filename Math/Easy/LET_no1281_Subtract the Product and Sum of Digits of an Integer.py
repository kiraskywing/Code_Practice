class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a, b = 1, 0
        while n > 0:
            val = n % 10
            a *= val
            b += val
            n //= 10

        return a - b