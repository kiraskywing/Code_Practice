class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        
        m, n = len(grid), len(grid[0])
        steps = 1
        queue = collections.deque([(0, 0)])
        grid[0][0] = 1
        
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if i == m - 1 and j == n - 1:
                    return steps
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        i2, j2 = i + di, j + dj
                        if 0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] == 0:
                            queue.append((i2, j2))
                            grid[i2][j2] = 1
            steps += 1
        
        return -1