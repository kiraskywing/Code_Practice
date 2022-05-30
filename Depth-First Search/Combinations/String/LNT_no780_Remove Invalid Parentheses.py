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

        if left < 0 or right < 0:
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


class Solution2:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left_remove = right_remove = 0
        for c in s:
            if c == '(':
                left_remove += 1
            elif c == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1
        
        res = set()
        self.dfs(s, 0, 0, 0, left_remove, right_remove, [], res)
        return list(res)
    
    def dfs(self, s, i, left, right, left_remove, right_remove, temp, res):
        if i == len(s):
            if left == right:
                res.add(''.join(temp))
            return
        
        if s[i] == '(':
            if left_remove > 0:
                self.dfs(s, i + 1, left, right, left_remove - 1, right_remove, temp, res)
            temp.append('(')
            self.dfs(s, i + 1, left + 1, right, left_remove, right_remove, temp, res)
            temp.pop()
        elif s[i] == ')':
            if right_remove > 0:
                self.dfs(s, i + 1, left, right, left_remove, right_remove - 1, temp, res)
            if left > right:
                temp.append(')')
                self.dfs(s, i + 1, left, right + 1, left_remove, right_remove, temp, res)
                temp.pop()
        else:
            temp.append(s[i])
            self.dfs(s, i + 1, left, right, left_remove, right_remove, temp, res)
            temp.pop()