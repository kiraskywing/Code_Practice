class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        s_backs = t_backs = 0
        
        while True:
            while i >= 0 and (s_backs > 0 or s[i] == '#'):
                s_backs += 1 if s[i] == '#' else -1
                i -= 1
            while j >= 0 and (t_backs > 0 or t[j] == '#'):
                t_backs += 1 if t[j] == '#' else -1
                j -= 1
            if not (i >= 0 and j >= 0 and s[i] == t[j]):
                return i == j == -1
            i -= 1
            j -= 1