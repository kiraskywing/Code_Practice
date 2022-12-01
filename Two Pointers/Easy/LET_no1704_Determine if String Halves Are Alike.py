class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = 0
        memo = set('aeiouAEIOU')
        i, j = 0, len(s) - 1
        while i < j:
            vowels += s[i] in memo
            vowels -= s[j] in memo
            i += 1
            j -= 1
            
        return vowels == 0