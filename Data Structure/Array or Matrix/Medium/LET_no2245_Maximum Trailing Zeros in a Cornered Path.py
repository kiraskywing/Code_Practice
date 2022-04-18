class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        sweep_rows = [[[0, 0] for _ in range(n)] for _ in range(m)]
        sweep_cols = [[[0, 0] for _ in range(n)] for _ in range(m)]
                    # [twos, fives]
        
        # twos and fives prefix_sum, row and col direction
        for i in range(m):
            for j in range(n):
                twos, fives = self.countTwosFives(grid[i][j])
                grid[i][j] = [twos, fives]
                if j == 0:
                    sweep_rows[i][j] = [twos, fives]
                else:
                    sweep_rows[i][j][0] = sweep_rows[i][j - 1][0] + twos
                    sweep_rows[i][j][1] = sweep_rows[i][j - 1][1] + fives
        for j in range(n):
            for i in range(m):
                twos, fives = grid[i][j]
                if i == 0:
                    sweep_cols[i][j] = [twos, fives]
                else:
                    sweep_cols[i][j][0] = sweep_cols[i - 1][j][0] + twos
                    sweep_cols[i][j][1] = sweep_cols[i - 1][j][1] + fives
        
        res = 0
        for i in range(m):
            for j in range(n):
                a, b = sweep_cols[m - 1][j]
                d, e = sweep_rows[i][n - 1]
                x, y = grid[i][j]
                a1, b1 = sweep_cols[i][j]
                a2, b2= sweep_rows[i][j]
                tmp = [a1 + a2 - x, b1 + b2 - y]
                res = max(res, min(tmp))
                tmp = [d - a2 + a1, e - b2 + b1]
                res = max(res, min(tmp))             
                tmp = [a - a1 + a2, b - b1 + b2]
                res = max(res, min(tmp))
                tmp = [a + d - a1 - a2 + x, b + e - b1 - b2 + y]
                res = max(res, min(tmp))
                          
        return res
                
    def countTwosFives(self, val):
        twos, fives = 0, 0
        while val % 2 == 0:
            twos += 1
            val //= 2
        while val % 5 == 0:
            fives += 1
            val //= 5
        return twos, fives
    