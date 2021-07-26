class Solution:
    def findIntegers(self, n: int) -> int:
        f = [0] * 32
        f[0], f[1] = 1, 2
        for i in range(2, 32):
            f[i] = f[i - 1] + f[i - 2]
            
        n += 1
        res, preBit = 0, False
        for k in range(30, -1, -1):
            if n & (1 << k):
                res += f[k]
                if preBit:
                    return res
                preBit = True
            else:
                preBit = False
        return res