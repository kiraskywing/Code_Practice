class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        pattern = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    pattern.add(self.bfs(grid, i, j, m, n))
        
        return len(pattern)
    
    def bfs(self, grid, i0, j0, m, n):
        memo = [0, 0]
        queue = collections.deque([(i0, j0)])
        grid[i0][j0] = 0
        
        while queue:
            i, j = queue.popleft()
            for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                i2, j2 = i + di, j + dj
                if 0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] == 1:
                    grid[i2][j2] = 0
                    memo.extend([i2 - i0, j2 - j0])
                    queue.append((i2, j2))
        
        return tuple(memo)