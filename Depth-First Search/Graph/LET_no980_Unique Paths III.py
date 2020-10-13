class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n, empty = len(grid), len(grid[0]), 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x, y = i, j
                if grid[i][j] == 0:
                    empty += 1
        self.res = 0
        self.dfs(grid, x, y, empty)
        return self.res
    
    def dfs(self, grid, x, y, empty):
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] >= 0):
            return
        if grid[x][y] == 2:
            self.res += empty == 0
            return
        grid[x][y] = -2
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            self.dfs(grid, x + dx, y + dy, empty - 1)
        grid[x][y] = 0
        