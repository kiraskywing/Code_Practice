class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        
        dp = [[0] * n for _ in range(n)]
        for d in range(1, n):
            for i in range(n - d):
                j = i + d
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        
        return dp[0][-1] > 0

# dp[i][j] means the biggest number of stones you can get more than opponent picking piles in piles[i] ~ piles[j].
# You can first pick piles[i] or piles[j].
# If you pick piles[i], your result will be piles[i] - dp[i + 1][j]
# If you pick piles[j], your result will be piles[j] - dp[i][j - 1]

class Solution2:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [0] * n
        
        for d in range(1, n):
            for i in range(n - d):
                j = i + d
                dp[i] = max(piles[i] - dp[j], piles[j] - dp[i])
        
        return dp[0] > 0