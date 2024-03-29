class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[1] * 6] + [[0] * 6 for _ in range(n)]
        
        # dp[n][k] means the number of strings constructed by at most k different characters.
        for i in range(1, n + 1):
            for k in range(1, 6):
                dp[i][k] = dp[i][k - 1] + dp[i - 1][k]
        
        return dp[-1][-1]

class Solution2:
    def countVowelStrings(self, n: int) -> int:
        dp = [0] + [1] * 5
        for _ in range(1, n + 1):
            for vowels in range(1, 6):
                dp[vowels] +=  dp[vowels - 1]
        
        return dp[-1]