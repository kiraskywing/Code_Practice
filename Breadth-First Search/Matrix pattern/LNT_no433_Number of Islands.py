class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """

    def numIslands(self, grid):

        if not grid or not grid[0]:
            return 0

        num_of_island = 0
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    num_of_island += 1

        return num_of_island

    def bfs(self, grid, x, y, visited):

        queue = collections.deque([(x, y)])
        visited.add((x, y))

        while queue:
            x, y = queue.popleft()

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_x = x + dx
                new_y = y + dy

                if not self.is_valid(grid, new_x, new_y, visited):
                    continue

                queue.append((new_x, new_y))
                visited.add((new_x, new_y))

    def is_valid(self, grid, x, y, visited):
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
            return False
        if (x, y) in visited:
            return False
        return grid[x][y]