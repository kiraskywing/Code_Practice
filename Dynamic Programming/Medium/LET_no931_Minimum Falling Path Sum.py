class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(n):
                prev = matrix[i - 1][j]
                if j < n - 1 and n > 1:
                    prev = min(prev, matrix[i - 1][j + 1])
                if j > 0 and n > 1:
                    prev = min(prev, matrix[i - 1][j - 1])
                matrix[i][j] += prev
        
        return min(matrix[-1])
