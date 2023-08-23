class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])
        while True:
            to_crush = set()
            for i in range(m):
                for j in range(n):
                    if board[i][j] != 0:
                        if i >= 2 and board[i - 2][j] == board[i - 1][j] == board[i][j]:
                            to_crush |= {(i - 2, j), (i - 1, j), (i, j)}
                        if j >= 2 and board[i][j - 2] == board[i][j - 1] == board[i][j]:
                            to_crush |= {(i, j - 2), (i, j - 1), (i, j)}

            if not to_crush:
                break
            
            for i, j in to_crush:
                board[i][j] = 0
            
            for j in range(n):
                idx = m - 1
                for i in range(m - 1, -1, -1):
                    if board[i][j] != 0:
                        board[i][j], board[idx][j] = board[idx][j], board[i][j]
                        idx -= 1
        
        return board