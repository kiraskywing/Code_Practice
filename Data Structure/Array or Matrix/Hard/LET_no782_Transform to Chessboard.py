class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        for i in range(n):
            for j in range(n):
                if board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]:
                    return -1
        
        rSum = cSum = rMiss = cMiss = 0
        for i in range(n):
            rSum += board[i][0]
            cSum += board[0][i]
            rMiss += board[i][0] == i % 2
            cMiss += board[0][i] == i % 2
        
        if rSum != n // 2 and rSum != (n + 1) // 2 or cSum != n // 2 and cSum != (n + 1) // 2:
            return -1
        
        if n % 2:
            if rMiss % 2: rMiss = n - rMiss
            if cMiss % 2: cMiss = n - cMiss
        else:
            rMiss = min(rMiss, n - rMiss)
            cMiss = min(cMiss, n - cMiss)
        
        return (rMiss + cMiss) // 2