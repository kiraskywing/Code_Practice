class Solution:
    def countHomogenous(self, s: str) -> int:
        res = count = 0
        mod = 10 ** 9 + 7
        cur = ' '
        for c in s:
            count = count + 1 if cur == c else 1
            res = (res + count) % mod
            cur = c
        
        return res