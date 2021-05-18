class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = collections.defaultdict(int)
        for w in sorted(words, key=len):
            dp[w] = max(dp[w[:i] + w[i+1:]] + 1 for i in range(len(w)))
        
        return max(dp.values())