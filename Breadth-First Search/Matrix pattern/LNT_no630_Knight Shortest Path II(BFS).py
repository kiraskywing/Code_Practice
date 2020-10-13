class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """

    def shortestPath2(self, grid):
        queue = collections.deque([(0, 0)])
        distance = {(0, 0): 0}
        m, n = len(grid), len(grid[0])

        while queue:
            x, y = queue.popleft()

            if x == m - 1 and y == n - 1:
                return distance[(x, y)]

            for dx, dy in [(1, 2), (-1, 2), (2, 1), (-2, 1)]:
                x2, y2 = x + dx, y + dy
                if 0 <= x2 < m and 0 <= y2 < n and grid[x2][y2] != 1 and (x2, y2) not in distance:
                    distance[(x2, y2)] = distance[(x, y)] + 1
                    queue.append((x2, y2))
        return -1