class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = {(x, y): float('inf') if i else 0 for i, (x, y) in enumerate(points)}
        res = 0
        while dist:
            x, y = min(dist, key=dist.get)
            res += dist.pop((x, y))
            for x2, y2 in dist:
                dist[(x2, y2)] = min(dist[(x2, y2)], abs(x - x2) + abs(y - y2))
        
        return res