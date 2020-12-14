class Solution:
    def maxPower(self, s: str) -> int:
        res = cur = 1
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur += 1
                res = max(res, cur)
            else:
                cur = 1
        
        return res