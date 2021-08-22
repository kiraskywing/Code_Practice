class Solution:
    def __init__(self):
        self.rows = [[False] * 9 for _ in range(9)]
        self.cols = [[False] * 9 for _ in range(9)]
        self.blocks = [[False] * 9 for _ in range(9)]
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    k = i // 3 * 3 + j // 3
                    self.rows[i][num] = self.cols[j][num] = self.blocks[k][num] = True
                    
        self.solver(board, 0, 0)
    
    def solver(self, board, i, j):
        if i == 9:
            return True
        if j == 9:
            return self.solver(board, i + 1, 0)
        if board[i][j] != '.':
            return self.solver(board, i, j + 1)
        
        k = i // 3 * 3 + j // 3
        for num in range(9):
            if self.check(i, j, k, num):
                self.rows[i][num] = self.cols[j][num] = self.blocks[k][num] = True
                board[i][j] = chr(ord('1') + num)
                if self.solver(board, i, j + 1):
                    return True
                board[i][j] = '.'
                self.rows[i][num] = self.cols[j][num] = self.blocks[k][num] = False
        
        return False
    
    def check(self, i, j, k, num):
        return not (self.rows[i][num] or self.cols[j][num] or self.blocks[k][num])