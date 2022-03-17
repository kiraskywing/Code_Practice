from typing import (
    List,
)

class Solution:
    """
    @param matrix: A 2D-array of integers
    @return: an integer
    """
    def longest_continuous_increasing_subsequence2(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        res = 0
        memo = {}
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                res = max(res, self.dfs(matrix, m, n, memo, i, j))
        return res

    def dfs(self, matrix, m, n, memo, i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        steps = 1
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            i2, j2 = i + di, j + dj
            if 0 <= i2 < m and 0 <= j2 < n and matrix[i2][j2] > matrix[i][j]:
                steps = max(steps, self.dfs(matrix, m, n, memo, i2, j2) + 1)
        memo[(i, j)] = steps
        
        return steps


class Solution2:
    """
    @param matrix: A 2D-array of integers
    @return: an integer
    """
    def longest_continuous_increasing_subsequence2(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        points = []
        for i in range(m):
            for j in range(n):
                points.append((matrix[i][j], i, j))
        points.sort()

        memo = {}
        res = 0
        for val, i, j in points:
            memo[(i, j)] = 1
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                i2, j2 = i + di, j + dj
                if 0 <= i2 < m and 0 <= j2 < n and matrix[i2][j2] < val and (i2, j2) in memo:
                    memo[(i, j)] = max(memo[(i, j)], memo[(i2, j2)] + 1)
            res = max(res, memo[(i, j)])
        return res
