class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        connected = collections.defaultdict(set)
        for i, j in roads:
            connected[i].add(j)
            connected[j].add(i)
        
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                res = max(res, len(connected[i]) + len(connected[j]) - (i in connected[j]))
        
        return res