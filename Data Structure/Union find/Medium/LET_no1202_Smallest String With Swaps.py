class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa != pb:
            self.parent[pb] = pa

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n)
        for a, b in pairs:
            uf.union(a, b)
            
        memo = collections.defaultdict(list)
        for i in range(n):
            memo[uf.find(i)].append(s[i])
        for key in memo:
            memo[key].sort(reverse=True)
        
        res = []
        for i in range(n):
            res.append(memo[uf.find(i)].pop())
            
        return ''.join(res)