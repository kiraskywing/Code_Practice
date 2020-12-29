class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = []
        
        for j in range(n):
            res.append(self.dfs(0, j, grid, m, n))
        
        return res
    
    def dfs(self, i, j, grid, m, n):
        if i == m:
            return j
        
        j2 = j + grid[i][j]
        if j2 < 0 or j2 >= n or grid[i][j] != grid[i][j2]:
            return -1
        
        return self.dfs(i + 1, j2, grid, m, n)