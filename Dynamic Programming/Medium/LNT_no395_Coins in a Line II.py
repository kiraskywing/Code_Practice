# Similar to LeetCode no.1406 Stone Game III

from typing import (
    List,
)

class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def first_will_win(self, values: List[int]) -> bool:
        n = len(values)
        if n <= 2:
            return True

        pre_sum = [0] * 3
        dp = [0] * 3
        dp[(n - 1) % 3] = pre_sum[(n - 1) % 3] = values[n - 1]
        for i in range(n - 2, -1, -1):
            pre_sum[i % 3] = pre_sum[(i + 1) % 3] + values[i]
            dp[i % 3] = max(
                values[i] + pre_sum[(i + 1) % 3] - dp[(i + 1) % 3],
                values[i] + values[i + 1] + pre_sum[(i + 2) % 3] - dp[(i + 2) % 3]
            )

        return dp[0] > pre_sum[0] - dp[0]

class Solution2:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def first_will_win(self, values: List[int]) -> bool:
        n = len(values)
        if n <= 2:
            return True

        dp = [0] * 2
        for i in range(n - 1, -1, -1):
            dp[i % 2] = max(sum(values[i:i+k]) - dp[(i + k) % 2] for k in (1, 2))
        return dp[0] > 0