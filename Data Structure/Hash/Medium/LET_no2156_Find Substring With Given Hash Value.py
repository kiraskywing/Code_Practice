class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        def getVal(c):
            return ord(c) - ord('a') + 1
        def fastPow(a, b, n):
            res = 1
            while n:
                if n & 1:
                    res = res * a % b
                a = a * a % b
                n >>= 1
            return res % b
        
        n = len(s)
        order = fastPow(power, modulo, k)
        
        res = n
        cur = 0
        for i in range(n - 1, -1, -1):
            cur = (cur * power + getVal(s[i])) % modulo
            if i + k < n:
                cur = (cur - getVal(s[i + k]) * order) % modulo
            if cur == hashValue:
                res = i
        return s[res:res+k]