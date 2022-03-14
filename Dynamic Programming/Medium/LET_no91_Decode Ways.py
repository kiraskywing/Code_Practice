class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        pre1, pre2, cur = 1, 1, 0
        for i in range(2, len(s) + 1):
            if 10 <= int(s[i-2:i]) <= 26:
                cur += pre2
            if 0 < int(s[i - 1]) <= 9:
                cur += pre1
            pre2, pre1, cur = pre1, cur, 0
        return pre1

class Solution2:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        dp = [0 for _ in range(n + 1)]
        dp[0] = dp[1] = 1
        for i in range(2, len(s) + 1):
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i - 2]
            if 0 < int(s[i-1]) <= 9:
                dp[i] += dp[i - 1]
        return dp[-1]