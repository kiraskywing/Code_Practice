from typing import (
    List,
)

class Solution:
    """
    @param a: An integer array
    @param target: An integer
    @return: An integer
    """
    def min_adjustment_cost(self, a: List[int], target: int) -> int:
        n = len(a)
        dp = [[float('inf')] * 101 for _ in range(n + 1)]
        # dp[i+1][j]表示元素A[i]=j时，A[i]与A[i-1]差值不大于target所需要付出的最小代价

        for j in range(101):
            dp[0][j] = 0

        for i in range(n + 1):
            for j in range(1, 101):
                left, right = max(1, j - target), min(100, j + target)
                for k in range(left, right + 1):
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + abs(j - a[i - 1]))
                    # 当A[i-2]=k时，答案为A[i-2]=k的代价dp[i-1][k]，加上A[i-1]=j的调整代价abs(j-A[i-1])
    
        return min(dp[n - 1])