class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = {}
        return min(self.dfs(grid, moveCost, 0, j, m - 1, n, memo) for j in range(n))
    
    def dfs(self, grid, moveCost, i, j, i_end, n, memo):
        if i == i_end:
            return grid[i][j]
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        value = grid[i][j]
        memo[(i, j)] = min(
            value + moveCost[value][j2] + self.dfs(grid, moveCost, i + 1, j2, i_end, n, memo) for j2 in range(n)
        )
        return memo[(i, j)]