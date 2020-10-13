class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 0

        queue = collections.deque([(0, 0, k, 0)])
        visited = {(0, 0, k)}

        while queue:
            x, y, eliminates, steps = queue.popleft()
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x2, y2 = x + dx, y + dy
                if 0 <= x2 < m and 0 <= y2 < n:
                    if grid[x2][y2] == 1 and eliminates > 0 and (x2, y2, eliminates - 1) not in visited:
                        visited.add((x2, y2, eliminates - 1))
                        queue.append((x2, y2, eliminates - 1, steps + 1))
                    if grid[x2][y2] == 0 and (x2, y2, eliminates) not in visited:
                        if x2 == m - 1 and y2 == n - 1:
                            return steps + 1
                        visited.add((x2, y2, eliminates))
                        queue.append((x2, y2, eliminates, steps + 1))

        return -1