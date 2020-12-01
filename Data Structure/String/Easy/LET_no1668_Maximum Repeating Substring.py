class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        res = cur = 0
        n, N = len(word), len(sequence)
        i = 0
        
        while i < N - (n - 1):
            if sequence[i : i + n] == word:
                cur += 1
                i += n
            else:
                res = max(res, cur)
                cur = 0
                i += 1
        res = max(res, cur)
        
        return res