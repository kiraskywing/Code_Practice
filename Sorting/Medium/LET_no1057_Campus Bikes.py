class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        memo = collections.defaultdict(list)
        d_min, d_max = float('inf'), float('-inf')
        for i in range(len(workers)):
            for j in range(len(bikes)):
                d = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                memo[d].append((i, j))
                d_min, d_max = min(d_min, d), max(d_max, d)
        
        res = [-1] * len(workers)
        bike_used = [False] * len(bikes)
        for d in range(d_min, d_max + 1):
            if d in memo:
                for i, j in memo[d]:
                    if res[i] == -1 and not bike_used[j]:
                        res[i] = j
                        bike_used[j] = True
        
        return res