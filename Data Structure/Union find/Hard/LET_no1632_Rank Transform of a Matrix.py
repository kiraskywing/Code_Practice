class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        record = collections.defaultdict(list)
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                record[matrix[i][j]].append((i, j))
        
        ranks = [0 for i in range(m + n)]
        for d in sorted(record):
            ranks2 = ranks[:]
            uf = UnionFind(m + n)
            
            for i, j in record[d]:
                i, j = uf.union(i, m + j)
                ranks2[j] = max(ranks2[i], ranks2[j])
            
            for i, j in record[d]:
                ranks[i] = ranks[m + j] = matrix[i][j] = ranks2[uf.find(i)] + 1
        
        return matrix
        
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        self.parent[pi] = pj
        return pi, pj