class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for s in strs:
            count = collections.Counter(s)
            for i in range(m, count['0'] - 1, -1):
                for j in range(n, count['1'] - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - count['0']][j - count['1']] + 1)
        
        return dp[m][n]