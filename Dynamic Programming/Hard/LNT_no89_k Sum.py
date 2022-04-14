from typing import (
    List,
)

class Solution:
    """
    @param a: An integer array
    @param k: A positive integer (k <= length(A))
    @param target: An integer
    @return: An integer
    """
    def k_sum(self, a: List[int], k: int, target: int) -> int:
        n = len(a)
        dp = [[[0] * (target + 1) for _ in range(k + 1)] for _ in range(n + 1)]

        # dp[i][j][m]: 前i個物品挑j個總和為m的方案數
        dp[0][0][0] = 1
        for i in range(1, n + 1):
            dp[i][0][0] = 1
            for j in range(1, min(i + 1, k + 1)):
                for m in range(1, target + 1):
                    dp[i][j][m] = dp[i - 1][j][m]
                    if m >= a[i - 1]:
                        dp[i][j][m] += dp[i - 1][j - 1][m - a[i - 1]]
        
        return dp[n][k][target]

class Solution2:
    def k_sum(self, a: List[int], k: int, target: int) -> int:
        n = len(a)
        dp = [[[0] * (target + 1) for _ in range(k + 1)] for _ in range(2)]

        # dp[i][j][m]: 前i個物品挑j個總和為m的方案數
        prev, cur = 1, 0
        dp[cur][0][0] = 1
        for i in range(1, n + 1):
            prev, cur = cur, prev
            dp[cur][0][0] = 1
            for j in range(1, min(i + 1, k + 1)):
                for m in range(1, target + 1):
                    dp[cur][j][m] = dp[prev][j][m]
                    if m >= a[i - 1]:
                        dp[cur][j][m] += dp[prev][j - 1][m - a[i - 1]]
        
        return dp[cur][k][target]

class Solution3:
    def k_sum(self, a: List[int], k: int, target: int) -> int:
        n = len(a)
        dp = [[0] * (target + 1) for _ in range(k + 1)]

        dp[0][0] = 1
        for i in range(n):
            for j in range(k, 0, -1):
                for m in range(target, a[i - 1] - 1, -1):
                    dp[j][m] += dp[j - 1][m - a[i - 1]]
        
        return dp[k][target]