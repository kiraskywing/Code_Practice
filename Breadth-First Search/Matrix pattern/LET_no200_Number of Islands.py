class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    self.bfs(grid, m, n, i, j)
        return res
    
    def bfs(self, grid, m, n, i, j):
        queue = collections.deque([(i, j)])
        while queue:
            i, j = queue.popleft()
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                i2, j2 = i + di, j + dj
                if 0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] == '1':
                    grid[i2][j2] = '0'
                    queue.append((i2, j2))