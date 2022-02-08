class Solution:
    """
    @param n: a non-negative integer
    @return: the total number of full staircase rows that can be formed
    """
    def arrangeCoins(self, n):
        left, right = 1, n
        while left + 1 < right:
            mid = (left + right) // 2
            cur = mid * (mid + 1) // 2
            if cur > n:
                right = mid
            else:
                left = mid
        if right * (1 + right) // 2 <= n:
            return right
        return left
