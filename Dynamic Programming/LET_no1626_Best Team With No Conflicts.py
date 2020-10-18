class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        rec = sorted(zip(ages, scores))
        n = len(rec)
        dp = [0] * n
        
        for i in range(n):
            dp[i] = rec[i][1]
            for j in range(i):
                if rec[j][1] <= rec[i][1]:
                    dp[i] = max(dp[i], dp[j] + rec[i][1])
        
        return max(dp)