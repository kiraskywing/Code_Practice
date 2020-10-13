class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """

    def shortestDistance(self, grid):
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])

        dist = [[sys.maxsize for _ in range(n)] for _ in range(m)]
        count = [[0 for _ in range(n)] for _ in range(m)]
        ans = sys.maxsize

        buildings = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j, dist, m, n, count)
                    buildings += 1

        for i in range(m):
            for j in range(n):
                if count[i][j] == buildings and dist[i][j] < ans:
                    ans = dist[i][j]

        return ans if ans != sys.maxsize else -1

    def bfs(self, grid, i, j, dist, m, n, count):
        visited = [[False for _ in range(n)] for _ in range(m)]
        visited[i][j] = True
        queue = collections.deque([(i, j, 0)])

        while queue:
            x, y, l = queue.popleft()
            if dist[x][y] == sys.maxsize:
                dist[x][y] = 0
            dist[x][y] += l

            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                x2, y2 = x + dx, y + dy

                if 0 <= x2 < m and 0 <= y2 < n and not visited[x2][y2]:
                    visited[x2][y2] = True
                    if grid[x2][y2] == 0:
                        queue.append((x2, y2, l + 1))
                        count[x2][y2] += 1