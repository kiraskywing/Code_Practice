class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        dp = [[0] * n for _ in range(n)]
        
        pre_sum = [0]
        for num in stones:
            pre_sum.append(pre_sum[-1] + num)
        
        for left in range(n - 2, -1, -1):
            for right in range(left + 1, n):
                dp[left][right] = max(pre_sum[right + 1] - pre_sum[left + 1] - dp[left + 1][right], pre_sum[right] - pre_sum[left] - dp[left][right - 1])
        #    Alice gain: a1 + a3 + a5 + ...
        #    Bob gain: b2 + b4 + b6 + ...
        #    final = a1 - (b2 - (a3 - (b4 - (a5 - a6))))
        #          = cur_gain - sub_problem_gain
        
        return dp[0][n  - 1]