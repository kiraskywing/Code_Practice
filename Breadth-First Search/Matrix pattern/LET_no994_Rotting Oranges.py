class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        freshes = 0
        minutes = 0
        queue = collections.deque([])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    freshes += 1
                    
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    i2, j2 = i + di, j + dj
                    if 0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] == 1:
                        freshes -= 1
                        grid[i2][j2] = 2
                        queue.append((i2, j2))
            if queue:
                minutes += 1
        
        return minutes if freshes == 0 else -1