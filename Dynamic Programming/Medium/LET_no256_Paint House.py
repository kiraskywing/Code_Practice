class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        for i in range(1, len(costs)):
            for j in range(3):
                costs[i][j] += min(costs[i - 1][j2] for j2 in range(3) if j2 != j)
        
        return min(costs[-1])