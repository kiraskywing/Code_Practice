from typing import (
    List,
)

class Solution:
    """
    @param a: an integer array
    @param v: an integer array
    @param m: An integer
    @return: an array
    """
    def back_pack_i_i_i(self, a: List[int], v: List[int], m: int) -> int:
        dp = [0] * (m + 1)
        dp[0] = 0
        for i in range(len(a)):
            for w in range(a[i], m + 1):
                dp[w] = max(dp[w], dp[w - a[i]] + v[i])
        return dp[-1]
