class Solution:
    def minOperations(self, n: int) -> int:
        h = n // 2
        return h * h + h if n % 2 else h * h