class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        caps = 0
        for c in word:
            caps += 'A' <= c <= 'Z'
        return caps == len(word) or (caps == 1 and 'A' <= word[0] <= 'Z') or caps == 0