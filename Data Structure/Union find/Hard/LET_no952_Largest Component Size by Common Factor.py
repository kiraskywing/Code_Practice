class unionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        self.parent[px] = py

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)
        uf = unionFind(n)
        primes = collections.defaultdict(list)
        for i, num in enumerate(nums):
            for p in self.getPrimes(num):
                primes[p].append(i)
        
        for _, indexes in primes.items():
            for i in range(len(indexes) - 1):
                uf.union(indexes[i], indexes[i + 1])
                
        return max(Counter([uf.find(i) for i in range(n)]).values())    
    
    def getPrimes(self, x):
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return self.getPrimes(x // i) | set([i])
        return set([x])