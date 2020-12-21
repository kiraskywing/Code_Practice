class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        res = [None] * len(queries)
        edgeList.sort(key=lambda x: x[2])
        queries = sorted([q + [i] for i, q in enumerate(queries)], key=lambda x: x[2])
        
        un = UnionFind(n)
        i = 0
        
        for a, b, limit, idx in queries:
            while i < len(edgeList) and edgeList[i][2] < limit:
                x, y, d = edgeList[i]
                un.union(x, y)
                i += 1
            res[idx] = un.find(a) == un.find(b)
        
        return res
    
    
class UnionFind:
    def __init__(self, N):
        self.root = list(range(N))
    
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, a, b):
        rx, ry = self.find(a), self.find(b)
        if rx != ry:
            self.root[ry] = rx
            return
    