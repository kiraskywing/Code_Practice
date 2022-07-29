class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        col_sum = [0] * n
        res = 0
        
        for i in range(m):
            row_sum = 0
            for j in range(n):
                if j == 0 or grid[i][j - 1] == 'W':
                    row_sum = 0
                    k = j
                    while k < n and grid[i][k] != 'W':
                        row_sum += grid[i][k] == 'E'
                        k += 1
                if i == 0 or grid[i - 1][j] == 'W':
                    col_sum[j] = 0
                    k = i
                    while k < m and grid[k][j] != 'W':
                        col_sum[j] += grid[k][j] == 'E'
                        k += 1
                if grid[i][j] =='0':
                    res = max(res, row_sum + col_sum[j])
        
        return res