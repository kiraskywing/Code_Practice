class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid):
        if not grid or not grid[0]:
            return -1

        queue = collections.deque([])
        humans, days = 0, 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    humans += 1
                if grid[i][j] == 1:
                    queue.append((i, j))
        if humans == 0:
            return days
        
        while queue:
            days += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    i2, j2 = i + di, j + dj
                    if 0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] == 0:
                        humans -= 1
                        if humans == 0:
                            return days
                        grid[i2][j2] = 1
                        queue.append((i2, j2))
        
        return -1
