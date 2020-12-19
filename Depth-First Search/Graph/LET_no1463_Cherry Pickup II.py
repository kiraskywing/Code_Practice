class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        return self.dfs(grid, dict(), 0, 0, 0, len(grid[0]) - 1)
    
    def dfs(self, grid, memo, i1, j1, i2, j2):
        if (i1, j1, i2, j2) in memo:
            return memo[(i1, j1, i2, j2)]
        
        res = 0
        for d1 in (-1, 0, 1):
            for d2 in (-1, 0, 1):
                x1, x2, y1, y2 = i1 + 1, i2 + 1, j1 + d1, j2 + d2
                if x1 < len(grid) and 0 <= y1 < len(grid[0]) and 0 <= y2 < len(grid[0]):
                    res = max(res, self.dfs(grid, memo, x1, y1, x2, y2))
        
        if j1 == j2:
            res += grid[i1][j1]
        else:
            res += (grid[i1][j1] + grid[i2][j2])
        memo[(i1, j1, i2, j2)] = res
        return res