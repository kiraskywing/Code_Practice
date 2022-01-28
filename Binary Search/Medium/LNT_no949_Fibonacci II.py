class Solution:
    """
    @param n: an integer
    @return: return an int
    """
    def lastFourDigitsOfFn(self, n):
        if n == 0:
            return 0
        
        a0, a1 = 0, 1
        base = [[1, 1], [1, 0]]
        res = self.fastPow(base, n)
        return (res[1][0] * a1 + res[1][1] * a0) % 10000
    
    def mul(self, a, b):
        res = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    res[i][j] += a[i][k] * b[k][j]
                    res[i][j] %= 10000
        return res
    
    def fastPow(self, base, n):
        res = [[1, 0], [0, 1]]
        while n:
            if n & 1:
                res = self.mul(res, base)
            base = self.mul(base, base)
            n >>= 1
        return res