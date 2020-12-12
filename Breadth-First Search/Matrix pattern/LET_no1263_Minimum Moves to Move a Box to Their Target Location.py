class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        self.n = len(grid)
        self.m = len(grid[0])

        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == "B":
                    x_B, y_B = i, j
                if grid[i][j] == "S":
                    x_S, y_S = i, j
        grid[x_B][y_B], grid[x_S][y_S] = ".", "."
        cur_level = {(x_B, y_B, x_S, y_S)}

        visited = set()
        moves = 0

        while cur_level:
            next_level = set()

            for i_B, j_B, i_S, j_S in cur_level:
                visited.add((i_B, j_B, i_S, j_S))

                if grid[i_B][j_B] == "T":
                    return moves

                for i_B2, j_B2, i_S2, j_S2 in self.valid_moves(grid, i_B, j_B, i_S, j_S):
                    if (i_B2, j_B2, i_S2, j_S2) not in visited:
                        next_level.add((i_B2, j_B2, i_S2, j_S2))

            cur_level = next_level
            moves += 1

        return -1

    def valid_moves(self, grid, x_B, y_B, x_S, y_S):
        next_moves = []

        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            r1, c1 = x_B + dx, y_B + dy
            r2, c2 = x_B - dx, y_B - dy

            if 0 <= r1 < self.n and 0 <= c1 < self.m and grid[r1][
                c1] != "#" and 0 <= r2 < self.n and 0 <= c2 < self.m and grid[r2][c2] != "#":
                if self.bfs_to_reach_box(grid, r1, c1, x_B, y_B, x_S, y_S):
                    next_moves.append((r2, c2, x_B, y_B))

        return next_moves

    def bfs_to_reach_box(self, grid, r, c, x_B, y_B, x_S, y_S):
        cur_level = {(r, c)}
        visited = set()

        while cur_level:
            next_level = set()

            for i, j in cur_level:
                visited.add((i, j))

                if i == x_S and j == y_S:
                    return True

                for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    i2, j2 = i + di, j + dj
                    if 0 <= i2 < self.n and 0 <= j2 < self.m and (i2, j2) not in visited and (i2, j2) != (x_B, y_B) and \
                            grid[i2][j2] != "#":
                        next_level.add((i2, j2))

            cur_level = next_level

        return False