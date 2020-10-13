DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]

class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """

    def zombie(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m, n = len(grid), len(grid[0])
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))

        day = 0
        while queue:
            day += 1
            for k in range(len(queue)):
                (x, y) = queue.popleft()
                for (dx, dy) in DIR:
                    x2, y2 = x + dx, y + dy
                    if 0 <= x2 < m and 0 <= y2 < n and grid[x2][y2] == 0:
                        grid[x2][y2] = 1
                        queue.append((x2, y2))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    return -1

        return day - 1
