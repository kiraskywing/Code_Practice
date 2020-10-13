class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """

    def generateParenthesis(self, n):
        if n == 0:
            return []

        result = []
        self.dfs(n, n, [], result)
        return result

    def dfs(self, left, right, temp, result):
        if left > right:
            return

        if left == 0 and right == 0:
            result.append(''.join(temp))

        if left > 0:
            temp.append("(")
            self.dfs(left - 1, right, temp, result)
            temp.pop()
        if right > 0:
            temp.append(")")
            self.dfs(left, right - 1, temp, result)
            temp.pop()
