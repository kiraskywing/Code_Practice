# The same as LeetCode no79. Word Search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.helper(board, i, j, word, 0):
                    return True
        return False
    
    def helper(self, board, i, j, word, k):
        if board[i][j] != word[k]:
            return False
        if k == len(word) - 1:
            return True
        
        board[i][j] = '*'
        
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            i2, j2 = i + di, j + dj
            if 0 <= i2 < len(board) and 0 <= j2 < len(board[0]) and self.helper(board, i2, j2, word, k + 1):
                return True
        
        board[i][j] = word[k]
        
        return False