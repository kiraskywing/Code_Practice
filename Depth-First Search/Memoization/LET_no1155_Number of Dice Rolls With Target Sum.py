class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        self.mod = 10 ** 9 + 7
        return self.helper(n, k, target, {}) % self.mod
    
    def helper(self, n, k, target, memo):
        if n == 0:
            return 1 if target == 0 else 0
        
        if (n, k, target) not in memo:
            memo[(n, k, target)] = 0
            ways = 0
            for cur in range(1, min(k, target) + 1):
                ways += self.helper(n - 1, k, target - cur, memo)
                ways %= self.mod
                
            memo[(n, k, target)] = ways
            
        return memo[(n, k, target)]