from typing import (
    Set,
)

class Solution:
    """
    @param s: A string
    @param dict: A set of word
    @return: the number of possible sentences.
    """
    def word_break3(self, s: str, dict: Set[str]) -> int:
        if not dict:
            return 0

        max_len, wordset = self.getWordSet(dict)
        return self.dfs(s.lower(), 0, max_len, wordset, {})

    def getWordSet(self, words):
        max_len = float('-inf')
        memo = set()
        for w in words:
            memo.add(w.lower())
            max_len = max(max_len, len(w))
        return max_len, memo
    
    def dfs(self, s, i, max_len, wordset, memo):
        if i == len(s):
            return 1
        if i in memo:
            return memo[i]
        
        memo[i] = 0
        for size in range(1, min(max_len, len(s) - i) + 1):
            if s[i:i+size] in wordset:
                memo[i] += self.dfs(s, i + size, max_len, wordset, memo)
        return memo[i]