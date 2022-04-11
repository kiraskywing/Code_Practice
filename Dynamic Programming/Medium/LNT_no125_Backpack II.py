from typing import (
    List,
)

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @param v: Given n items with value V[i]
    @return: The maximum value
    """
    def back_pack_i_i(self, m: int, a: List[int], v: List[int]) -> int:
        if m == 0 or not a or not v:
            return 0
        
        n = len(a)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if j >= a[i - 1]:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - a[i - 1]] + v[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[n][-1]

class Solution2:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @param v: Given n items with value V[i]
    @return: The maximum value
    """
    def back_pack_i_i(self, m: int, a: List[int], v: List[int]) -> int:
        if m == 0 or not a or not v:
            return 0
        
        n = len(a)
        dp = [[0] * (m + 1) for _ in range(2)]
        cur, prev = 0, 1
        for i in range(1, n + 1):
            cur, prev = prev, cur
            for j in range(1, m + 1):
                if j >= a[i - 1]:
                    dp[cur][j] = max(dp[prev][j], dp[prev][j - a[i - 1]] + v[i - 1])
                else:
                    dp[cur][j] = dp[prev][j]
        
        return dp[cur][-1]

class Solution3:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @param v: Given n items with value V[i]
    @return: The maximum value
    """
    def back_pack_i_i(self, m: int, a: List[int], v: List[int]) -> int:
        if m == 0 or not a or not v:
            return 0
        
        n = len(a)
        dp = [0] * (m + 1)
        for i in range(1, n + 1):
            for j in range(m, a[i - 1] - 1, -1):
                dp[j] = max(dp[j], dp[j - a[i - 1]] + v[i - 1])
        
        return dp[-1]