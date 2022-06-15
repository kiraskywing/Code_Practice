class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = collections.defaultdict(int)
        for w in sorted(words, key=len):
            dp[w] = max(dp[w[:i] + w[i+1:]] + 1 for i in range(len(w)))
        
        return max(dp.values())

class Solution2:
    def longestStrChain(self, words: List[str]) -> int:
        word_set = set(words)
        return max(self.helper(w, word_set, {}) for w in words)
    
    def helper(self, w, word_set, memo):
        if w in memo:
            return memo[w]
        
        memo[w] = 1
        nxt = 0
        for i in range(len(w)):
            w2 = w[:i] + w[i + 1:]
            if w2 in word_set:
                nxt = max(nxt, self.helper(w2, word_set, memo))
        
        memo[w] += nxt
        return memo[w]