from typing import (
    List,
)

class Solution:
    """
    @param matrix: a matrix of 0 an 1
    @return: an integer
    """
    def max_square2(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        left_zeros = [[0] * (n + 1) for _ in range(m + 1)]
        up_zeros = [[0] * (n + 1) for _ in range(m + 1)]
        diagonal = [[0] * (n + 1) for _ in range(m + 1)]

        res = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == 0:
                    diagonal[i][j] = 0
                    left_zeros[i][j] = left_zeros[i][j - 1] + 1
                    up_zeros[i][j] = up_zeros[i - 1][j] + 1
                else:
                    diagonal[i][j] = min(diagonal[i - 1][j - 1], left_zeros[i][j - 1], up_zeros[i - 1][j]) + 1
                    left_zeros[i][j] = up_zeros[i][j] = 0
                
                res = max(res, diagonal[i][j])
        
        return res ** 2
