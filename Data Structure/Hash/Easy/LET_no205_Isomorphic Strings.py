class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t = dict()
        used_t = set()
        
        for i in range(len(s)):
            if s[i] in s2t and s2t[s[i]] != t[i]:
                return False
            elif s[i] not in s2t:
                s2t[s[i]] = t[i]
                if t[i] in used_t:
                    return False
                used_t.add(t[i])
        
        return True