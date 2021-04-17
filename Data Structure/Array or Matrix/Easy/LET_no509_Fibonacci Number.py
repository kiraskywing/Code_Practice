class Solution:
    def fib(self, n: int) -> int:
        a0, a1 = 0, 1
        mat = self.fast_power(n)
        return mat[1][0] * a1 + mat[1][1] * a0
    
    def fast_power(self, n):
        base = [[1, 1], [1, 0]]
        res = [[1, 0], [0, 1]]
        while n:
            if n & 1:
                res = self.mat_p(res, base)
            base = self.mat_p(base, base)
            n //= 2
        return res
                
    def mat_p(self, a, b):
        temp = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    temp[i][j] += a[i][k] * b[k][j]
        return temp