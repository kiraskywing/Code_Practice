class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = 0
        
        uf = UnionFind(len(edges))
        for a, b in edges:
            if uf.find(a) != uf.find(b):
                uf.union(a, b)
            else:
                return [a, b]
        
        return []
        
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        self.parent[px] = py