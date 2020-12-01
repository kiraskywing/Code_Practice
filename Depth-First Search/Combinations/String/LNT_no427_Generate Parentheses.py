# The same as Leetcode no.22 Generate Parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.helper(res, "", 0, 0, n)
        return res
    
    def helper(self, res, string, left_used, right_used, length):
        if len(string) == length * 2:
            res.append(string)
            return
        
        if left_used < length:
            self.helper(res, string + '(', left_used + 1, right_used, length)
        if right_used < left_used:
            self.helper(res, string + ')', left_used, right_used + 1, length)