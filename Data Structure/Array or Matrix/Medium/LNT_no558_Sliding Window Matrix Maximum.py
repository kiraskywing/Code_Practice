from typing import (
    List,
)

class Solution:
    """
    @param matrix: an integer array of n * m matrix
    @param k: An integer
    @return: the maximum number
    """
    def max_sliding_matrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        if m < k or n < k:
            return 0
        
        pre_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                pre_sum[i + 1][j + 1] = pre_sum[i][j + 1] + pre_sum[i + 1][j] - pre_sum[i][j] + matrix[i][j]
        
        res = float('-inf')
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                res = max(res, pre_sum[i + k][j + k] - pre_sum[i][j + k] - pre_sum[i + k][j] + pre_sum[i][j])
        return res