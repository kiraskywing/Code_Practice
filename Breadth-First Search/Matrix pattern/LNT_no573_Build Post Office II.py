# The same as LeetCode no317. Shortest Distance from All Buildings

from typing import (
    List,
)

class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """
    def shortest_distance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist = [[0] * n for _ in range(m)]
        buildings = [[0] * n for _ in range(m)]
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
                    self.bfs(grid, dist, buildings, m, n, i, j)
        
        res = float('inf')
        for i in range(m):
            for j in range(n):
                if buildings[i][j] == count:
                    res = min(res, dist[i][j])

        return res if res != float('inf') else -1

    def bfs(self, grid, dist, buildings, m, n, i, j):
        visited = [[False] * n for _ in range(m)]
        queue = collections.deque([(i, j, 1)])
        
        while queue:
            i, j, d = queue.popleft()
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                i2, j2 = i + di, j + dj
                if 0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] == 0 and not visited[i2][j2]:
                    visited[i2][j2] = True
                    buildings[i2][j2] += 1
                    dist[i2][j2] += d
                    queue.append((i2, j2, d + 1))
