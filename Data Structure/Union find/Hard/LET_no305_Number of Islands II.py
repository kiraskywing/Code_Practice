class UnionFind:
    def __init__(self):
        self.parent = dict()
        self.count = 0
        
    def add(self, i, j):
        self.parent[(i, j)] = (i, j)
        self.count += 1
    
    def find(self, i, j):
        if self.parent[(i, j)] != (i, j):
            i2, j2 = self.parent[(i, j)]
            self.parent[(i, j)] = self.find(i2, j2)
        return self.parent[(i, j)]
    
    def union(self, i, j, i2, j2):
        p1i, p1j = self.find(i, j)
        p2i, p2j = self.find(i2, j2)
        if (p1i, p1j) != (p2i, p2j):
            self.count -= 1
            self.parent[(p2i, p2j)] = (p1i, p1j)

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = UnionFind()
        res = []
        
        for i, j in positions:
            if (i, j) not in uf.parent:
                uf.add(i, j)
                for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    i2, j2 = i + di, j + dj
                    if 0 <= i2 < m and 0 <= j2 < n and (i2, j2) in uf.parent:
                        uf.union(i, j, i2, j2)
            
            res.append(uf.count)
        
        return res
