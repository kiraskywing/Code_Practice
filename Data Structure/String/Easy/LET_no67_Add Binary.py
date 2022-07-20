class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a), len(b)
        res = []
        cur = 0
        i, j = m - 1, n - 1
        while i >= 0 or j >= 0:
            if i >= 0:
                cur += int(a[i])
                i -= 1
            if j >= 0:
                cur += int(b[j])
                j -= 1
            res.append(str(cur % 2))
            cur //= 2
        
        if cur > 0:
            res.append(str(cur))
        
        return ''.join(res[::-1])