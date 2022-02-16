# The same as LeetCode no301. Remove Invalid Parentheses

class Solution:
    """
    @param s: The input string
    @return: Return all possible results
    """

    def removeInvalidParentheses(self, s):
        result = []
        left, right = self.count(s)
        self.dfs(s, left, right, 0, result)
        return result

    def dfs(self, string, left, right, start, result):
        if left == 0 and right == 0:
            if self.is_valid(string):
                result.append(string)
            return

        for i in range(start, len(string)):
            if i > start and string[i] == string[i - 1]:
                continue

            if string[i] == "(":
                self.dfs(string[:i] + string[i + 1:], left - 1, right, i, result)
            if string[i] == ")":
                self.dfs(string[:i] + string[i + 1:], left, right - 1, i, result)

    def count(self, string):
        left, right = 0, 0
        for ch in string:
            if ch == "(":
                left += 1
            if ch == ")":
                if left > 0:
                    left -= 1
                else:
                    right += 1
        return left, right

    def is_valid(self, string):
        left, right = self.count(string)
        return left == 0 and right == 0
