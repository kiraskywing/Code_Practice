class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = [1 for _ in range(n)]

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa != pb:
            if self.count[pa] < self.count[pb]:
                pa, pb = pb, pa
            self.count[pa] += self.count[pb]
            self.parent[pb] = pa

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        
        uf = UnionFind(n)
        prime_to_idx = {}

        for i, num in enumerate(nums):
            if num == 1:
                return False
            
            prime = 2
            while prime * prime <= num:
                if num % prime == 0:
                    if prime in prime_to_idx:
                        uf.union(i, prime_to_idx[prime])
                    else:
                        prime_to_idx[prime] = i
                    while num % prime == 0:
                        num //= prime
                prime += 1
            
            if num > 1:
                if num in prime_to_idx:
                    uf.union(i, prime_to_idx[num])
                else:
                    prime_to_idx[num] = i
        
        return uf.count[uf.find(0)] == n