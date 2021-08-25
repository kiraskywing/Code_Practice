class Solution:
    """
    @param grid: a matrix
    @return: Find all points that are strictly larger than their neighbors
    """
    def highpoints(self, grid):
        # write your code here
        m, n = len(grid), len(grid[0])
        res = [[0] * n for _ in range(m)]
        dirs = [(dx, dy) for dx in range(-1, 2) for dy in range(-1, 2)]

        for i in range(m):
            for j in range(n):
                check = 1
                for di, dj in dirs:
                    i2, j2 = i + di, j + dj
                    if 0 <= i2 < m and 0 <= j2 < n and (i2 != i or j2 != j) and grid[i][j] <= grid[i2][j2]:
                        check = 0
                        break
                res[i][j] = check
        
        return res