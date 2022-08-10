class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        
        s = s.strip()
        res, neg = 0, 1
        max_val, min_val = 2 ** 31 - 1, -(2 ** 31)
        
        for i in range(len(s)):
            if i == 0 and s[i] in "-+":
                if s[i] == '-':
                    neg = -1
                continue
            if '0' <= s[i] <= '9':
                res = res * 10 + ord(s[i]) - ord('0')
            else:
                break
        
        res *= neg
        if res > max_val:
            return max_val
        if res < min_val:
            return min_val
        return res

class Solution2:
    def myAtoi(self, s: str) -> int:
        res = 0
        sign = 1
        i = 0
        
        while i < len(s) and s[i] == ' ':
            i += 1
        if i < len(s) and s[i] in '+-':
            sign = -1 if s[i] == '-' else 1
            i += 1
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
        
        res *= sign
        upper, lower = 2 ** 31 - 1, -(2 ** 31)
        if res < lower:
            return lower
        if res > upper:
            return upper
        return res