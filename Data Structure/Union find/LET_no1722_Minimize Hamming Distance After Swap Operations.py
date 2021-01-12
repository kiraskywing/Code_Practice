class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        uf = UnionFind(n)
        for u, v in allowedSwaps:
            uf.union(u, v)
        
        table = collections.defaultdict(set)
        for i in range(n):
            table[uf.find(i)].add(i)
        
        res = 0
        for indices in table.values():
            A = collections.Counter(source[i] for i in indices)
            B = collections.Counter(target[i] for i in indices)
            res += sum((A - B).values())
        
        return res

class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
    
    def union(self, u, v):
        self.root[self.find(u)] = self.find(v)
    
    def find(self, i):
        if i != self.root[i]:
            self.root[i] = self.find(self.root[i])
        return self.root[i]