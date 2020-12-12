class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        if k == 0:
            return grid

        n, m = len(grid), len(grid[0])
        result = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                number = j + i * m
                final_number = (number + k) % (m * n)
                j_2 = final_number % m
                i_2 = final_number // m
                result[i_2][j_2] = grid[i][j]

        return result