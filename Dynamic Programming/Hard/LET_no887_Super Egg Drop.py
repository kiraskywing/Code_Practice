class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
        
        for steps in range(1, n + 1):
            for remain_eggs in range(1, k + 1):
                dp[steps][remain_eggs] = dp[steps - 1][remain_eggs - 1] + dp[steps - 1][remain_eggs] + 1
            if dp[steps][k] >= n:
                return steps
        return 0