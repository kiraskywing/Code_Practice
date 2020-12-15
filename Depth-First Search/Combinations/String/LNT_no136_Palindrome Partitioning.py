# The same as Leetcode no131 Palindrome Partitioning

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(res, [], s)
        return res
    
    def dfs(self, res, temp, s):
        if not s:
            res.append(temp[:])
            return
        
        for i in range(1, len(s) + 1):
            if self.is_palindrome(s[:i]):
                temp.append(s[:i])
                self.dfs(res, temp, s[i:])
                temp.pop()
    
    def is_palindrome(self, s):
        return s == s[::-1]