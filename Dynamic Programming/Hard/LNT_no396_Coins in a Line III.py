from typing import (
    List,
)

class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def first_will_win(self, values: List[int]) -> bool:
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = values[i]
        
        for length in range(1, n):
            for left in range(n - length):
                right = left + length
                dp[left][right] = max(values[left] - dp[left + 1][right], values[right] - dp[left][right - 1])
        
        return dp[0][n - 1] > 0
