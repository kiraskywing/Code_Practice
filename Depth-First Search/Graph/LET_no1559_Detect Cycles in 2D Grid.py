class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = set()
        
        for i in range(m):
            for j in range(n):
                if (i, j) in visited:
                    continue
                if self.dfs(grid, visited, (i, j), None):
                    return True
        return False
    
    def dfs(self, grid, visited, node, parent):
        if node in visited:
            return True
        
        visited.add(node)
        x, y = node
        
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            x2, y2 = x + dx, y + dy
            if not self.valid_pos(grid, visited, x, y, x2, y2, parent):
                continue
            if self.dfs(grid, visited, (x2, y2), node):
                return True
        
        return False
    
    def valid_pos(self, grid, visited, x, y, x2, y2, parent):
        if not (0 <= x2 < len(grid) and 0 <= y2 < len(grid[0])):
            return False
        if grid[x][y] != grid[x2][y2]:
            return False
        if (x2, y2) == parent:
            return False
        return True