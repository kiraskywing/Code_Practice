class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        uf = UnionFind(n + 1)
        for i in range(threshold + 1, n + 1):
            for j in range(i * 2, n + 1, i):
                if i > threshold: uf.union(i, j)
        
        ans = []
        for a, b in queries:
            pa, pb = uf.find(a), uf.find(b)
            ans.append(pa == pb)
        return ans

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    def find(self, x):
        if x != self.parent[x]: self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        self.parent[pu] = pv