class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        queue = collections.deque([])
        for i in range(m):
            if board[i][0] == 'O':
                board[i][0] = '*'
                queue.append((i, 0))
            if board[i][n - 1] == 'O':
                board[i][n - 1] = '*'
                queue.append((i, n - 1))
        for i in range(n):
            if board[0][i] == 'O':
                board[0][i] = '*'
                queue.append((0, i))
            if board[m - 1][i] == 'O':
                board[m - 1][i] = '*'
                queue.append((m - 1, i))
                
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x2, y2 = x + dx, y + dy
                if 0 <= x2 < m and 0 <= y2 < n and board[x2][y2] == 'O':
                    board[x2][y2] = '*'
                    queue.append((x2, y2))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O': board[i][j] = 'X'
                elif board[i][j] == '*': board[i][j] = 'O'