class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = n
    
    def findParent(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.findParent(self.parent[i])
        return self.parent[i]
    
    def union2one(self, i, j):
        pi, pj = self.findParent(i), self.findParent(j)
        if pi != pj:
            self.parent[pj] = pi
            self.count -= 1
            if self.count == 1:
                return True
        return False

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        uf = UnionFind(n)
        for date, i, j in logs:
            if uf.union2one(i, j):
                return date
        return -1