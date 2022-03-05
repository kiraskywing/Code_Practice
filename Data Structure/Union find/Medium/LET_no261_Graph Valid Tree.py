class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
#         root = i
#         while root != self.parent[root]:
#             root = self.parent[root]
        
#         while i != self.parent[i]:
#             old_root = self.parent[i]
#             self.parent[i] = root
#             i = old_root
        
#         return root
    
    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        
        self.parent[pb] = pa
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        uf = UnionFind(n)
        for a, b in edges:
            if not uf.union(a, b):
                return False
        
        return True