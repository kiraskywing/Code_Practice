class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1, num2 = list(num1[::-1]), list(num2[::-1])
        m, n = len(num1), len(num2)
        res = [0] * (m + n + 1)
        
        for i in range(m):
            for j in range(n):
                cur = int(num1[i]) * int(num2[j]) + res[i + j]
                res[i + j] = cur % 10
                res[i + j + 1] += cur // 10
                
        for k in range(m + n, -1, -1):
            if res[k] != 0:
                return ''.join(str(d) for d in res[:k+1])[::-1]
        
        return '0'

class Solution2:
    def multiply(self, num1: str, num2: str) -> str:
        num1, num2 = int(num1), int(num2)
        return str(self.karatsuba(num1, num2))
    
    def karatsuba(self, num1, num2):
        if num1 < 10 and num2 < 10:
            return num1 * num2
        
        digits = max(len(str(num1)), len(str(num2)))
        half = math.ceil(digits / 2)
        spliter = 10 ** half
        
        num1_H, num1_L = num1 // spliter, num1 % spliter
        num2_H, num2_L = num2 // spliter, num2 % spliter
        
        a = self.karatsuba(num1_H, num2_H)
        b = self.karatsuba(num1_L, num2_L)
        c = self.karatsuba(num1_H + num1_L, num2_H + num2_L) - a - b
        
        return a * (10 ** (half * 2)) + c * (10 ** half) + b