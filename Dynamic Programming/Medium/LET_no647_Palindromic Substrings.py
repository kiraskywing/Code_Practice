class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        res = 0
            
        for d in range(n):
            for left in range(n - d):
                right = left + d
                dp[left][right] = s[left] == s[right] and (right - left < 3 or dp[left + 1][right - 1])
                res += dp[left][right]
        
        return res