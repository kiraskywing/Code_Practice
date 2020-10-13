class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 0
        
        res = cur = 0
        dis = [sys.maxsize] * n
        used = set()
        
        for _ in range(n - 1):
            x, y = points[cur]
            used.add(cur)
            for i, (x2, y2) in enumerate(points):
                if i in used:
                    continue
                dis[i] = min(dis[i], abs(x2 - x) + abs(y2 - y))
            
            delta, cur = min((d, i) for i, d in enumerate(dis))
            dis[cur] = sys.maxsize
            res += delta
        
        return res
            
            