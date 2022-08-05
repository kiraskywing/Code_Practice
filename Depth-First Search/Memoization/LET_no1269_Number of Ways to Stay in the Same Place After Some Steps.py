class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        memo = {}
        return self.dfs(0, steps, arrLen, memo)
    
    def dfs(self, pos, steps, size, memo):
        if not (0 <= pos < size) or pos > steps:
            return 0
        if pos == steps:
            return 1
        
        if (pos, steps) not in memo:
            memo[(pos, steps)] = (self.dfs(pos - 1, steps - 1, size, memo) + 
                                  self.dfs(pos + 1, steps - 1, size, memo) +
                                  self.dfs(pos, steps - 1, size, memo)) % (10 ** 9 + 7)
        return memo[(pos, steps)]