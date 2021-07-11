class Solution:
    def numDecodings(self, s: str) -> int:
        mod = 10 ** 9 + 7
        e, e1, e2 = 1, 0, 0
        
        for c in s:
            if c == '*':
                f = e * 9 + e1 * 9 + e2 * 6
                f1 = e
                f2 = e
            else:
                f = (c > '0') * e + e1 + (c <= '6') * e2
                f1 = (c == '1') * e
                f2 = (c == '2') * e
            e, e1, e2 = f % mod, f1, f2
        
        return e