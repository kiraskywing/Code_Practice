class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        return self.isMatch(pattern, 0, s, 0, {}, set())
    
    def isMatch(self, p, i, s, j, mapping, used_words):
        if i == len(p):
            return j == len(s)
        
        c = p[i]
        if c in mapping:
            cur_s = mapping[c]
            if not s[j:].startswith(cur_s):
                return False
            return self.isMatch(p, i + 1, s, j + len(cur_s), mapping, used_words)
        
        for j2 in range(j + 1, len(s) + 1):
            if s[j:j2] not in used_words:
                mapping[c] = s[j:j2]
                used_words.add(s[j:j2])
                if self.isMatch(p, i + 1, s, j2, mapping, used_words):
                    return True
                used_words.remove(s[j:j2])
                del mapping[c]
        
        return False