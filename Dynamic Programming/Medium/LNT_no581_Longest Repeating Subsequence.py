class Solution:
    """
    @param str: a string
    @return: the length of the longest repeating subsequence
    """
    def longest_repeating_subsequence(self, s: str) -> int:
        if not s:
            return 0
        
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if s[i] == s[j] and i != j:
                    dp[i][j] = dp[i - 1][j - 1] + 1 if i > 0 and j > 0 else 1
                else:
                    if i > 0 and j > 0:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[-1][-1]
