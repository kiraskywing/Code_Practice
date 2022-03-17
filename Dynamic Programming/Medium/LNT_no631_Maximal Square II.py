from typing import (
    List,
)

class Solution:
    """
    @param matrix: a matrix of 0 an 1
    @return: an integer
    """
    def max_square2(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        left_zeros = [[0] * n for _ in range(m)]
        up_zeros = [[0] * n for _ in range(m)]
        dp = [[0] * n for _ in range(m)]

        length = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                    left_zeros[i][j] = 1 if j == 0 else left_zeros[i][j - 1] + 1
                    up_zeros[i][j] = 1 if i == 0 else up_zeros[i - 1][j] + 1
                else:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j - 1], left_zeros[i][j - 1], up_zeros[i - 1][j]) + 1
                    left_zeros[i][j] = up_zeros[i][j] = 0
                    length = max(length, dp[i][j])
        
        return length ** 2
