# The same as LeetCode no52. N-Queens II

class Solution:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """

    def totalNQueens(self, n):

        visited, result = {}, []
        self.dfs(0, visited, n, result)
        return sum(result)

    def dfs(self, row, visited, n, result):
        if row == n:
            result.append(1)
            return

        for col in range(n):
            if col in visited:
                continue
            if self.attack(row, col, visited):
                continue

            visited[col] = row
            self.dfs(row + 1, visited, n, result)
            del visited[col]

    def attack(self, row, col, visited):
        for c in visited:
            if col - c == row - visited[c] or col - c == -(row - visited[c]):
                return True

        return False