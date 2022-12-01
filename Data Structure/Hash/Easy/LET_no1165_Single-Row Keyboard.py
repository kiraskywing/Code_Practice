class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        memo = {c:i for i, c in enumerate(keyboard)}
        prev = 0
        res = 0
        for c in word:
            cur = memo[c]
            res += abs(cur - prev)
            prev = cur
        
        return res