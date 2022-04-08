from typing import (
    List,
)

class Solution:
    """
    @param a: An integer array
    @return: An integer
    """
    def stone_game2(self, a: List[int]) -> int:
        n = len(a)
        if n == 0:
            return 0

        pre_sum = [0] * (2 * n + 1)
        dp = [[float('inf')] * (2 * n + 1) for _ in range(2 * n + 1)]
        for i in range(1, 2 * n + 1):
            pre_sum[i] = pre_sum[i - 1] + a[(i - 1) % n]
            dp[i][i] = 0

        for length in range(2, n + 1):
            for i in range(1, 2 * n + 1 - length):
                j = i + length - 1
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + pre_sum[j] - pre_sum[i - 1])
        
        res = float('inf')
        for i in range(1, n + 1):
            res = min(res, dp[i][i + n - 1])
        return res