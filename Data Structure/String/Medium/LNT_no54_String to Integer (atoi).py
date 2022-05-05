# The same as LeetCode no8. String to Integer (atoi)

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