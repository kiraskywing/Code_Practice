from typing import (
    List,
)

class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """
    def back_pack_i_v(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for num in nums:
            for i in range(num, target + 1):
                dp[i] += dp[i - num]
        return dp[target]
