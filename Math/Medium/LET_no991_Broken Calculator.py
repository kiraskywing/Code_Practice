class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        res = 0
        while Y > X:
            res += Y % 2 + 1
            Y = (Y + 1) // 2
        return res + X - Y