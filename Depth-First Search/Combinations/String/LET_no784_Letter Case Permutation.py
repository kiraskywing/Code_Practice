class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        S = list(S)
        self.helper(S, res, 0)
        return res
    
    def helper(self, string, res, i):
        if i == len(string):
            res.append(''.join(string))
            return
        
        if string[i].isdigit():
            self.helper(string, res, i + 1)
            return
        
        string[i] = string[i].lower()
        self.helper(string, res, i + 1)
        string[i] = string[i].upper()
        self.helper(string, res, i + 1)