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
        lefts, rights = self.countRemoves(s)
        res = []
        self.helper(s, 0, lefts, rights, [], res)
        return list(res)
    
    def helper(self, s, start, lefts, rights, temp, res):
        if lefts == 0 and rights == 0:
            cur = ''.join(s[i:j] for i, j in temp) + s[start:]
            if self.valid(cur):
                res.append(cur)
            return
        
        if lefts < 0 or rights < 0:
            return
        
        for i in range(start, len(s)):
            if i > start and s[i] == s[i - 1]:
                continue
                
            if s[i] == '(':
                temp.append((start, i))
                self.helper(s, i + 1, lefts - 1, rights, temp, res)
                temp.pop()
            elif s[i] == ')':
                temp.append((start, i))
                self.helper(s, i + 1, lefts, rights - 1, temp, res)
                temp.pop()
        
    def valid(self, s):
        lefts, rights = self.countRemoves(s)
        return lefts == 0 and rights == 0
    
    def countRemoves(self, s):
        lefts = rights = 0
        for c in s:
            if c == '(':
                lefts += 1
            elif c == ')':
                if lefts > 0:
                    lefts -= 1
                else:
                    rights += 1
        
        return lefts, rights