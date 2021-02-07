class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key = lambda x: x[1])
        dp, dp2 = [[0, 0]], [[0, 0]]
        
        for i in range(k):
            for start, end, value in events:
                i = bisect.bisect(dp, [start]) - 1
                if dp[i][1] + value > dp2[-1][1]:
                    dp2.append([end, dp[i][1] + value])
            dp, dp2 = dp2, [[0, 0]]
        
        return dp[-1][-1]