class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        i, j = len(num1) - 1, len(num2) - 1
        nxt = 0
        
        while i >= 0 or j >= 0:
            cur = nxt
            a = b = 0
            if i >= 0:
                a = ord(num1[i]) - ord('0')
                i -= 1
            if j >= 0:
                b = ord(num2[j]) - ord('0')
                j -= 1
            cur += a + b
            res.append(chr(cur % 10 + ord('0')))
            nxt = cur // 10
        
        if nxt:
            res.append('1')
        
        return ''.join(res)[::-1]