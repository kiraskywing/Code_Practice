class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n, empties = len(grid), len(grid[0]), 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x, y = i, j
                if grid[i][j] == 0:
                    empties += 1
        self.res = 0
        self.dfs(grid, x, y, empties)
        return self.res
    
    def dfs(self, grid, x, y, empties):
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] >= 0 and empties >= 0):
            return
        if grid[x][y] == 2:
            self.res += empties == 0
            return
        
        grid[x][y] = -2
        self.dfs(grid, x - 1, y, empties - 1)
        self.dfs(grid, x, y - 1, empties - 1)
        self.dfs(grid, x + 1, y, empties - 1)
        self.dfs(grid, x, y + 1, empties - 1)
        grid[x][y] = 0