class UnionFind:
    def __init__(self, points):
        self.parent = dict()
        for i, j in points:
            self.parent[i], self.parent[~j] = i, ~j
        
        self.size = len(self.parent)
    
    def find(self, x):
        root = x
        while root != self.parent[root]:
            root = self.parent[root]
        
        while x != self.parent[x]:
            temp = self.parent[x]
            self.parent[x] = root
            x = temp
        
        return root
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[px] = py
            self.size -= 1

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UnionFind(stones)
        for i, j in stones:
            uf.union(i, ~j)
        
        return len(stones) - uf.size