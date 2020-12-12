class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        row, col, di = [[0] * 3 for _ in range(2)], [[0] * 3 for _ in range(2)], [[0] * 2 for _ in range(2)]
        player = 0

        for r, c in moves:
            row[player][r] += 1
            col[player][c] += 1
            di[player][0] += r == c
            di[player][1] += r + c == 2
            if 3 in (row[player][r], col[player][c], di[player][0], di[player][1]):
                return 'AB'[player]
            player ^= 1

        return 'Draw' if len(moves) == 9 else 'Pending'