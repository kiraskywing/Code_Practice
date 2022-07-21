class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for u, v in edges:
            uf.union(u, v)
        return uf.size

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = n
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    # def find(self, i):
    #     res = i
    #     while self.parent[res] != res:
    #         res = self.parent[res]
    #     while self.parent[i] != res:
    #         i2 = self.parent[i]
    #         self.parent[i] = res
    #         i = i2
    #     return res
    
    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi != pj:
            self.parent[pj] = pi
            self.size -= 1