class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        cubs = [[0, 0, 0]] + sorted(map(sorted, cuboids))
        dp = [0] * len(cubs)
        
        for i in range(1, len(cubs)):
            for j in range(i):
                if all(cubs[j][k] <= cubs[i][k] for k in range(3)):
                    dp[i] = max(dp[i], dp[j] + cubs[i][2])
        
        return max(dp)