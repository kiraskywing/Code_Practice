class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if abs(m - n) > 1:
            return False
        
        for i in range(min(m, n)):
            if s[i] != t[i]:
                return s[i+1:] == t[i:] or s[i:] == t[i+1:] or s[i+1:] == t[i+1:]
        return m != n