class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = {}
        mod = 10 ** 9 + 7
        
        def helper(i, j, maxMove):
            if maxMove < 0:
                return 0
            if not (0 <= i < m and 0 <= j < n):
                return 1
            if (i, j, maxMove) in dp:
                return dp[(i, j, maxMove)]
            
            left = helper(i - 1, j, maxMove - 1) % mod
            right = helper(i + 1, j, maxMove - 1) % mod
            up = helper(i, j - 1, maxMove - 1) % mod
            down = helper(i, j + 1, maxMove - 1) % mod
            dp[(i, j, maxMove)] = (left + right + up + down) % mod
            
            return dp[(i, j, maxMove)]
        
        return helper(startRow, startColumn, maxMove)