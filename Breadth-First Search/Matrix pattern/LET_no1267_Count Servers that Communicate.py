class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        result = 0
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i, j) not in visited:
                    result += self.bfs(grid, i, j, visited)

        return result

    def bfs(self, grid, i, j, visited):
        queue = collections.deque([(i, j)])
        visited.add((i, j))
        connects = 1

        while queue:
            m, n = queue.popleft()

            for m2 in range(len(grid)):
                if grid[m2][n] and (m2, n) not in visited:
                    queue.append((m2, n))
                    visited.add((m2, n))
                    connects += 1
            for n2 in range(len(grid[0])):
                if grid[m][n2] and (m, n2) not in visited:
                    queue.append((m, n2))
                    visited.add((m, n2))
                    connects += 1

        return connects if connects > 1 else 0