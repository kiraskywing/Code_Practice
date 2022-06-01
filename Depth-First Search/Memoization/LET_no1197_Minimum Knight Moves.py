class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        return self.dfs(abs(x), abs(y), {})
    
    def dfs(self, x, y, memo):
        if (x, y) in memo:
            return memo[(x, y)]
        
        if x + y == 0:
            return 0
        elif x + y == 2:
            return 2
        memo[(x, y)] = min(self.dfs(abs(x - 2), abs(y - 1), memo), self.dfs(abs(x - 1), abs(y - 2), memo)) + 1
        return memo[(x, y)]