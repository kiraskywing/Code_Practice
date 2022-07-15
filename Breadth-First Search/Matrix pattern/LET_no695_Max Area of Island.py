class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, self.bfs(grid, i, j, m, n))
        
        return res
    
    def bfs(self, grid, i, j, m, n):
        queue = collections.deque([(i, j)])
        grid[i][j] = 0
        count = 1
        
        while queue:
            i, j = queue.popleft()
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                i2, j2 = i + di, j + dj
                if 0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] == 1:
                    grid[i2][j2] = 0
                    count += 1
                    queue.append((i2, j2))
        
        return count