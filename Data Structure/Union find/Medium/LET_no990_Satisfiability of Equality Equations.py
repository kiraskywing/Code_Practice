class UnionFind:
    def __init__(self):
        self.parent = dict()
        
    def find(self, i):
        if i not in self.parent:
            self.parent[i] = i
            return i
        
        cur = i
        while cur != self.parent[cur]:
            cur = self.parent[cur]
            
        while self.parent[i] != cur:
            nxt = self.parent[i]
            self.parent[i] = cur
            i = nxt
        
        return cur
    
    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        self.parent[pj] = pi

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind()
        
        for a, e, _, b in equations:
            if e == '=':
                uf.union(a, b)
            
        for a, e, _, b in equations:
            if e == '!':
                pa, pb = uf.find(a), uf.find(b)
                if pa == pb:
                    return False
        
        return True