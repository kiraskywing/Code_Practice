class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0] or grid[0][0] != 0:
            return -1
        
        m, n = len(grid), len(grid[0])
        queue = collections.deque([(0, 0, 1)])
        grid[0][0] = 1
        shift = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        while queue:
            x, y, k = queue.popleft()
            if x == m - 1 and y == n - 1:
                return k
            for dx, dy in shift:
                x2, y2 = x + dx, y + dy
                if 0 <= x2 <= m - 1 and 0 <= y2 <= n - 1 and grid[x2][y2] == 0:
                    grid[x2][y2] = 1
                    queue.append((x2, y2, k + 1))
        
        return -1