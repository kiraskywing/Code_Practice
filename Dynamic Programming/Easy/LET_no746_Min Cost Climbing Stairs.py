class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp  = [0] * len(cost)
        for i in range(len(cost)):
            if i <= 1:
                dp[i] = cost[i]
            else:
                dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        return min(dp[-1], dp[-2])

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])
        return cost[-1]