class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n, mod = len(grid), len(grid[0]), 10 ** 9 + 7
        dp = [[[None, None] for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = dp[0][0][1] = grid[0][0]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    dp[i][j][0] = dp[i][j][1] = grid[i][j] * dp[i][j - 1][0]
                elif j == 0:
                    dp[i][j][0] = dp[i][j][1] = grid[i][j] * dp[i - 1][j][0]
                else:
                    a = grid[i][j] * max(dp[i][j - 1][0], dp[i - 1][j][0])
                    b = grid[i][j] * min(dp[i][j - 1][1], dp[i - 1][j][1])
                    dp[i][j][0] = max(a, b)
                    dp[i][j][1] = min(a, b)
        
        if dp[m - 1][n - 1][0] < 0:
            return -1
        return dp[m - 1][n - 1][0] % mod