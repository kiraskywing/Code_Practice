from typing import (
    List,
)

class Solution:
    """
    @param a: an integer array
    @param k: An integer
    @return: an integer
    """
    def post_office(self, a: List[int], k: int) -> int:
        n = len(a)
        if n <= k:
            return 0

        a.sort()
        interval_sum = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                pos = a[(i + j) // 2]
                for h in range(i, j + 1):
                    interval_sum[i][j] += abs(a[h] - pos)

        dp = [[float('inf') for _ in range(n + 1)] for _ in range(k + 1)]
        for i in range(k + 1):
            for j in range(i + 1):
                dp[i][j] = 0
        for i in range(1, k + 1):
            for j in range(i + 1, n + 1):
                for pre_houses in range(1, j + 1):
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - pre_houses] + interval_sum[j - pre_houses][j - 1])
        
        return dp[-1][-1]
