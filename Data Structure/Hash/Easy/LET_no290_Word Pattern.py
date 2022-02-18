class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        memo, used = {}, set()
        for c, w in zip(pattern, words):
            if c not in memo:
                if w in used:
                    return False
                memo[c] = w
                used.add(w)
            elif memo[c] != w:
                return False
                
        return True