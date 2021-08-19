class Solution:
    def numDecodings(self, s: str) -> int:
        p, pp, n = 1, 0, len(s)
        for i in range(n - 1, -1, -1):
            cur = 0 if s[i] == '0' else p
            if i < n - 1 and (s[i] == '1' or (s[i] == '2' and int(s[i + 1]) < 7)):
                cur += pp
            pp = p
            p = cur
        
        return 0 if len(s) == 0 else p