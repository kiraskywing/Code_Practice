class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        memo = {}
        
        def dfs(i, groups, prev):
            if i == len(houses) and groups == 0:
                return 0
            if groups < 0 or m - i < groups:
                return float('inf')
            
            key = (i, groups, prev)
            
            if key not in memo:
                if houses[i] == 0:
                    memo[key] = min(dfs(i + 1, groups - int(prev != cur), cur) + cost[i][cur - 1] for cur in range(1, n + 1))
                else:
                    memo[key] = dfs(i + 1, groups - int(prev != houses[i]), houses[i])
            
            return memo[key]
        
        res = dfs(0, target, -1)
        return res if res != float('inf') else -1