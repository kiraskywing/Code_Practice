class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        used1 = [[False] * 9 for _ in range(9)]
        used2 = [[False] * 9 for _ in range(9)]
        used3 = [[False] * 9 for _ in range(9)]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    k = i // 3 * 3 + j // 3
                    if used1[i][num] or used2[j][num] or used3[k][num]:
                        return False
                    used1[i][num] = used2[j][num] = used3[k][num] = True
        
        return True