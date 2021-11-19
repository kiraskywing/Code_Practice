class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res, n = 0, x ^ y
        while n:
            res += 1
            n &= n - 1
        return res