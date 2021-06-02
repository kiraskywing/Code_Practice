class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]: self.bfs(grid, res, i, j)
        
        return max(res) if res else 0
    
    def bfs(self, grid, res, i, j):
        m, n = len(grid), len(grid[0])
        cur = 1
        grid[i][j] = 0
        queue = collections.deque([])
        queue.append((i, j))
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x2, y2 = x + dx, y + dy
                if 0 <= x2 < m and 0 <= y2 < n and grid[x2][y2]:
                    cur += 1
                    grid[x2][y2] = 0
                    queue.append((x2, y2))
        
        res.append(cur)