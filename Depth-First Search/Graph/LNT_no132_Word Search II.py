DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """

    def wordSearchII(self, board, words):

        if not board:
            return []

        word_set = set(words)
        prefix_set = set()

        for word in words:
            for i in range(len(word)):
                prefix_set.add(word[:i + 1])

        result = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                head = board[i][j]
                visited = set([(i, j)])  # set([()]) becomes a tuple set
                self.search(i, j, board, head, word_set, prefix_set, visited, result)

        return list(result)

    def search(self, x, y, board, word, word_set, prefix_set, visited, result):

        if word not in prefix_set:
            return
        if word in word_set:
            result.add(word)

        for delta_x, delta_y in DIRECTIONS:
            x2, y2 = x + delta_x, y + delta_y

            if not self.valid_coordinate(board, x2, y2):
                continue
            if (x2, y2) in visited:
                continue

            visited.add((x2, y2))
            self.search(x2, y2, board, word + board[x2][y2], word_set, prefix_set, visited, result)
            visited.remove((x2, y2))

    def valid_coordinate(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])