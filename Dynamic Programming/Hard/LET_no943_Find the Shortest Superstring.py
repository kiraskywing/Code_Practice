class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        shared = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(min(len(words[i]), len(words[j])), -1, -1):
                    if words[i][-k:] == words[j][:k]:
                        shared[i][j] = k
                        break
        
        dp = [[''] * 12 for _ in range(1 << 12)]
        for i in range(1 << n):
            for k in range(n):
                if not (i & (1 << k)):
                    continue
                if i == 1 << k:
                    dp[i][k] = words[k]
                    continue
                for j in range(n):
                    if j == k:
                        continue
                    if i & (1 << j):
                        s = dp[i ^ (1 << k)][j]
                        s += words[k][shared[j][k]:]
                        if dp[i][k] == '' or len(s) < len(dp[i][k]):
                            dp[i][k] = s
        
        min_len = float('inf')
        res = ''
        
        for i in range(n):
            s = dp[(1 << n) - 1][i]
            if len(s) < min_len:
                res, min_len = s, len(s)
        
        return res