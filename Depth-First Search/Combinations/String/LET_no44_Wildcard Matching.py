class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.helper(s, p, 0, 0, dict())

    def helper(self, s, p, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == len(s):
            if j == len(p):
                return True
            else:
                return set(p[j:]) == set('*')
        
        if j == len(p):
            return False

        res = False
        if p[j] == '*':
            res = self.helper(s, p, i + 1, j, memo) or self.helper(s, p, i, j + 1, memo)
        else:
            res = (p[j] in ('?', s[i])) and self.helper(s, p, i + 1, j + 1, memo)
        memo[(i, j)] = res

        return res
    