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
                    for k in range(j, n):
                        if grid[i][k] == 'W':
                            break
                        if grid[i][k] == 'E':
                            row_sum += 1
                if i == 0 or grid[i - 1][j] == 'W':
                    col_sum[j] = 0
                    for k in range(i, m):
                        if grid[k][j] == 'W':
                            break
                        if grid[k][j] == 'E':
                            col_sum[j] += 1
                if grid[i][j] == '0':
                    res = max(res, row_sum + col_sum[j])
                
        return res