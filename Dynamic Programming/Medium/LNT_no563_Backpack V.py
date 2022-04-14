from typing import (
    List,
)

class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """
    def back_pack_v(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        
        prefix_sum = 0
        for i in range(1, n + 1):
            dp[i][0] = 1
            prefix_sum += nums[i - 1]
            for cur in range(1, min(target, prefix_sum) + 1):
                dp[i][cur] = dp[i - 1][cur]
                if cur >= nums[i - 1]:
                    dp[i][cur] += dp[i - 1][cur - nums[i - 1]]
        
        return dp[n][target]

class Solution2:
    def back_pack_v(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[0] * (target + 1) for _ in range(2)]
        prev, cur = 0, 1
        dp[cur][0] = 1
        prefix_sum = 0
        for i in range(1, n + 1):
            prev, cur = cur, prev
            dp[cur][0] = 1
            prefix_sum += nums[i - 1]
            for val in range(1, min(target, prefix_sum) + 1):
                dp[cur][val] = dp[prev][val]
                if val >= nums[i - 1]:
                    dp[cur][val] += dp[prev][val - nums[i - 1]]
        
        return dp[cur][target]

class Solution3:
    def back_pack_v(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0] * (target + 1)
        dp[0] = 1
        prefix_sum = 0
        for i in range(1, n + 1):
            prefix_sum += nums[i - 1]
            for val in range(target, nums[i - 1] - 1, -1):
                dp[val] += dp[val - nums[i - 1]]
        
        return dp[target]