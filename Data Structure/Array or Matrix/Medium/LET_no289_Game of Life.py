class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # dead -> live: 2, live -> dead: 3
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                neighbors = sum(board[i2][j2] % 2 for i2 in range(i - 1, i + 2) for j2 in range(j - 1, j + 2) if 0 <= i2 < m and 0 <= j2 < n) - board[i][j]
                if board[i][j] == 0 and neighbors == 3:
                    board[i][j] = 2
                if board[i][j] == 1 and (neighbors < 2 or neighbors > 3):
                    board[i][j] = 3
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                if board[i][j] == 3:
                    board[i][j] = 0