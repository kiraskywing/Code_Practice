class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        memo = {}
        self.mod = 10 ** 9 + 7
        self.n = arrLen
        return self.dfs(0, steps, memo)
    
    def dfs(self, pos, steps, memo):
        if (pos, steps) in memo:
            return memo[(pos, steps)]
        
        if pos < 0 or pos == self.n or pos > steps:
            return 0
        if steps == pos:
            return 1
        
        memo[(pos, steps)] = (
            self.dfs(pos, steps - 1, memo) +
            self.dfs(pos - 1, steps - 1, memo) +
            self.dfs(pos + 1, steps - 1, memo)
        ) % self.mod
        
        return memo[(pos, steps)]
        