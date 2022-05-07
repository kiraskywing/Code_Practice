class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa != pb:
            self.parent[pa] = pb
            self.size[pb] += self.size[pa]

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        uf = UnionFind(len(nums))
        memo = {}
        
        for i, num in enumerate(nums):
            if num in memo:
                continue
            
            if num + 1 in memo:
                uf.union(i, memo[num + 1])
            if num - 1 in memo:
                uf.union(i, memo[num - 1])
            
            memo[num] = i
        
        return max(uf.size)