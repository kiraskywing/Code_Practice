class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        return self.is_match(pattern, 0, s, 0, {}, set())

    def is_match(self, s1, i, s2, j, memo, used_words):
        if i == len(s1):
            return j == len(s2)
        
        c = s1[i]
        if c in memo:
            word = memo[c]
            if not s2[j:].startswith(word):
                return False
            return self.is_match(s1, i + 1, s2, j + len(word), memo, used_words)

        for j2 in range(j + 1, len(s2) + 1):
            word = s2[j:j2]
            if word not in used_words:
                used_words.add(word)
                memo[c] = word
                if self.is_match(s1, i + 1, s2, j2, memo, used_words):
                    return True
                del memo[c]
                used_words.remove(word)
        
        return False