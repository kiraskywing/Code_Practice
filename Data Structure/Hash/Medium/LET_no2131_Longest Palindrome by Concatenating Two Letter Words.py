class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        memo = [[0 for _ in range(26)] for _ in range(26)]
        res = 0
        for w in words:
            a, b = ord(w[0]) - ord('a'), ord(w[1]) - ord('a')
            if memo[b][a] > 0:
                res += 4
                memo[b][a] -= 1
            else:
                memo[a][b] += 1
        
        for i in range(26):
            if memo[i][i] > 0:
                res += 2
                break
        
        return res