class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        return sum(self.test(s, t, m, n, 0, j) for j in range(n)) + sum(self.test(s, t, m, n, i, 0) for i in range(1, m))
        
    def test(self, s, t, m, n, i, j):
        pre = cur = res = 0
        for k in range(min(m - i, n - j)):
            cur += 1
            if s[i + k] != t[j + k]:
                pre = cur
                cur = 0
            res += pre
        return res