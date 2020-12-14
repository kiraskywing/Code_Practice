class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + [i for i in nums if i > 0] + [1] # 去掉0, 左右邊界加上[1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        # dp[i][j]: coins obtained from bursting all the balloons between index i and j (not including i or j)
        
        for k in range(2, n):    # k: swap range
            for left in range(n - k):
                right = left + k
                for i in range(left + 1, right):    # i: last ballon to burst
                    dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
                    # last burst: nums[left] * nums[i] * nums[right]
                    # dp[left][i]: coins otained from left to i (not including left or i)
                    # dp[i][right]: coins otained from i to right (not including i or right)
                    
        return dp[0][n - 1]