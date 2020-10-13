class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """

    def exist(self, board, word):
        if word == []:
            return True
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        if n == 0:
            return False

        visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if self.word_found(board, word, visited, i, j):
                    return True

        return False

    def word_found(self, board, word, visited, x, y):
        if word == '':
            return True

        if not (0 <= x < len(board)) or not (0 <= y < len(board[0])):
            return False

        if board[x][y] == word[0] and not visited[x][y]:
            visited[x][y] = True
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x2, y2 = x + dx, y + dy
                if self.word_found(board, word[1:], visited, x2, y2):
                    return True
            visited[x][y] = False
        return False
