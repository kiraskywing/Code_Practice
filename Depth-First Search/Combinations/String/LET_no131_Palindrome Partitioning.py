class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, 0, [], res)
        return res
    
    def dfs(self, s, start, temp, res):
        if start == len(s):
            res.append(temp[:])
            return
        
        for i in range(start, len(s)):
            if self.isPalindrome(s, start, i):
                temp.append(s[start:i+1])
                self.dfs(s, i + 1, temp, res)
                temp.pop()
    
    def isPalindrome(self, s, left, right):
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1
        return left >= right