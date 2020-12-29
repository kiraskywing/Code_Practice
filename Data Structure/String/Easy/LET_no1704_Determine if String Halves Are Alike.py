class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        res = 0
        vowels = set('aeiouAEIOU')
        i, j = 0, len(s) - 1
        while i < j:
            res += 1 if s[i] in vowels else 0
            res -= 1 if s[j] in vowels else 0
            i += 1
            j -= 1
        
        return res == 0