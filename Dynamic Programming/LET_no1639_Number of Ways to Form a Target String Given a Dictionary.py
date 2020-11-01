class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        m, n, k, mod = len(words), len(words[0]), len(target), 10 ** 9 + 7
        Q = [[0] * 26 for _ in range(n)]
        dp = [[0] * k for _ in range(n)]
        sp = [[0] * k for _ in range(n)]
        
        for i in range(n):         # source index
            for j in range(m):     # mth word
                Q[i][ord(words[j][i]) - ord('a')] += 1
        
        dp[0][0] = sp[0][0] = Q[0][ord(target[0]) - ord('a')]
        
        for i in range(1, n):     # source index
            for j in range(k):    # target index
                if j == 0:
                    dp[i][j] = Q[i][ord(target[j]) - ord('a')]
                else:
                    dp[i][j] = Q[i][ord(target[j]) - ord('a')] * sp[i - 1][j - 1]
                
                sp[i][j] = (sp[i - 1][j] + dp[i][j]) % mod
        
        return sp[-1][-1] % mod