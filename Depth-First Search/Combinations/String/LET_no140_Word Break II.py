class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.dfs(s, 0, set(wordDict), {})
    
    def dfs(self, s, i, wordDict, memo):
        if i == len(s):
            return []
        if i in memo:
            return memo[i]
        
        res = []
        for j in range(i + 1, len(s) + 1):
            cur = s[i:j]
            if cur not in wordDict:
                continue
            
            subs = self.dfs(s, j, wordDict, memo)
            for sub in subs:
                res.append(cur + ' ' + sub)
        
        if s[i:] in wordDict:
            res.append(s[i:])
        memo[i] = res
        return res