class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """

    def wordBreak(self, s, dict):
        if len(dict) == 0:
            return len(s) == 0

        n = len(s)
        valid = [False] * (n + 1)
        valid[0] = True
        max_len = max(len(word) for word in dict)

        for i in range(1, n + 1):
            for j in range(1, min(i, max_len) + 1):
                if not valid[i - j]:
                    continue
                if s[i - j: i] in dict:
                    valid[i] = True
                    break

        return valid[n]
    
class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        m = max(len(w) for w in wordDict)
        return self.helper(s, 0, m, wordDict, {})

    def helper(self, s, start, max_len, word_dict, memo):
        if start == len(s):
            return True
        
        if start not in memo:
            res = False
            for l in range(1, max_len + 1):
                sub = s[start:start+l]
                if sub in word_dict and self.helper(s, start + l, max_len, word_dict, memo):
                    res = True
            memo[start] = res
        
        return memo[start]