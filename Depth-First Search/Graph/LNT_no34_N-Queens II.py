# The same as LeetCode no52. N-Queens II

class Solution:
    def totalNQueens(self, n: int) -> int:
        return self.dfs(0, n, [])
    
    def dfs(self, row, n, temp):
        if row == n:
            return 1
        
        cur = 0
        for col in range(n):
            if self.valid(row, col, temp):
                temp.append(col)
                cur += self.dfs(row + 1, n, temp)
                temp.pop()
        return cur
                
    def valid(self, r, c, temp):
        for r2, c2 in enumerate(temp):
            if c == c2:
                return False
            if r + c == r2 + c2:
                return False
            if r - c == r2 - c2:
                return False
        return True