class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        return self.helper(s, seen)
    
    def helper(self, s, seen):
        if not s:
            return 0
        
        ans = 0
        for i in range(1, len(s) + 1):
            candidate = s[:i]
            if candidate not in seen:
                seen.add(candidate)
                ans = max(ans, 1 + self.helper(s[i:], seen))
                seen.remove(candidate)
        return ans