# The same as LeetCode no43. Multiply Strings

class Solution:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return product of num1 and num2
    """
    def multiply(self, num1, num2):
        m, n = len(num1), len(num2)
        res = ['0'] * (m + n)
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                cur = ord(res[i + j + 1]) - ord('0') + (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                res[i + j + 1] = chr(ord('0') + cur % 10)
                res[i + j] = chr(ord(res[i + j]) + cur // 10)
        
        
        for i in range(m + n):
            if res[i] != '0':
                return ''.join(res[i:])
        
        return '0'
