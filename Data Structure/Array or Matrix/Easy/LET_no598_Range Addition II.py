class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        a, b = m, n
        for x, y in ops:
            a, b = min(a, x), min(b, y)
        return a * b