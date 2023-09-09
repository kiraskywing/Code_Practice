class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        lefts, rights = self.to_remove(s)
        res = []
        self.helper(s, 0, lefts, rights, [], res)
        return res

    def helper(self, s, start, lefts, rights, temp, res):
        if lefts == 0 and rights == 0:
            cur = ''.join(s[i:j] for i, j in temp) + s[start:]
            if self.is_valid(cur):
                res.append(cur)
            return

        if lefts < 0 or rights < 0:
            return

        for end in range(start, len(s)):
            if end > start and s[end] == s[end - 1]:
                continue

            if s[end] == '(':
                temp.append((start, end))
                self.helper(s, end + 1, lefts - 1, rights, temp, res)
                temp.pop()
            elif s[end] == ')':
                temp.append((start, end))
                self.helper(s, end + 1, lefts, rights - 1, temp, res)
                temp.pop()

    def to_remove(self, s):
        lefts, rights = 0, 0
        for c in s:
            if c == '(':
                lefts += 1
            elif c == ')':
                if lefts > 0:
                    lefts -= 1
                else:
                    rights += 1
        
        return lefts, rights
    
    def is_valid(self, s):
        lefts, rights = self.to_remove(s)
        return lefts == 0 and rights == 0