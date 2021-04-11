class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        return max(self.dfs(dp, matrix, i, j, m, n) for i in range(m) for j in range(n))
    
    def dfs(self, dp, matrix, i, j, m, n):
        if dp[i][j] != 0: return dp[i][j]
        
        dp[i][j] = 1 + max(
        self.dfs(dp, matrix, i - 1, j, m, n) if i - 1 >= 0 and matrix[i][j] > matrix[i - 1][j] else 0,
        self.dfs(dp, matrix, i + 1, j, m, n) if i + 1 < m and matrix[i][j] > matrix[i + 1][j] else 0,
        self.dfs(dp, matrix, i, j - 1, m, n) if j - 1 >= 0 and matrix[i][j] > matrix[i][j - 1] else 0,
        self.dfs(dp, matrix, i, j + 1, m, n) if j + 1 < n and matrix[i][j] > matrix[i][j + 1] else 0)
        
        return dp[i][j]