class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        memo = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        self.helper(digits, 0, memo, [], res)
        return res

    def helper(self, s, start, memo, temp, res):
        if start == len(s):
            res.append(''.join(temp))
            return

        for c in memo[s[start]]:
            temp.append(c)
            self.helper(s, start + 1, memo, temp, res)
            temp.pop()