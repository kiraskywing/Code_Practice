class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0] * k for k in range(1, query_row + 3)]
        tower[0][0] = poured
        
        for row in range(query_row + 1):
            for col in range(row + 1):
                overflow = (tower[row][col] - 1) / 2
                if overflow > 0:
                    tower[row + 1][col] += overflow
                    tower[row + 1][col + 1] += overflow
        
        return min(1, tower[query_row][query_glass])