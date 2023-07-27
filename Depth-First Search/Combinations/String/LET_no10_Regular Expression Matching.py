class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.dfs(s, 0, p, 0, {})
    
    def dfs(self, s, i, p, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == len(s):
            return self.valid(p, j)
        if j == len(p):
            return False
        
        memo[(i, j)] = False
        if j < len(p) - 1 and p[j + 1] == '*':
            memo[(i, j)] = self.matchCheck(s[i], p[j]) and self.dfs(s, i + 1, p, j, memo) or self.dfs(s, i, p, j + 2, memo)
        else:
            memo[(i, j)] = self.matchCheck(s[i], p[j]) and self.dfs(s, i + 1, p, j + 1, memo)
            
        return memo[(i, j)]
    
    def matchCheck(self, a, b):
        return a == b or b == '.'
    
    def valid(self, p, start):
        if (len(p) - start) % 2 != 0:
            return False
        
        for i in range(start + 1, len(p), 2):
            if p[i] != '*':
                return False
        return True