class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        return self.helper(s1, 0, s2, 0, 0, {})
    
    def helper(self, s1, i, s2, j, diff, memo):
        if i == len(s1) and j == len(s2):
            return diff == 0
        
        if (i, j, diff) in memo:
            return memo[(i, j, diff)]
        
        memo[(i, j, diff)] = False
        
        if i < len(s1) and s1[i].isdigit():
            i2 = i
            while i2 < len(s1) and s1[i2].isdigit():
                i2 += 1
            for size in self.getPossibleSizes(s1[i:i2]):
                if self.helper(s1, i2, s2, j, diff - size, memo):
                    memo[(i, j, diff)] = True
                    
        elif j < len(s2) and s2[j].isdigit():
            j2 = j
            while j2 < len(s2) and s2[j2].isdigit():
                j2 += 1
            for size in self.getPossibleSizes(s2[j:j2]):
                if self.helper(s1, i, s2, j2, diff + size, memo):
                    memo[(i, j, diff)] = True
                    
        elif diff == 0 and i < len(s1) and j < len(s2) and s1[i] == s2[j]:
            memo[(i, j, diff)] = self.helper(s1, i + 1, s2, j + 1, diff, memo)
        elif diff > 0 and i < len(s1):
            memo[(i, j, diff)] = self.helper(s1, i + 1, s2, j, diff - 1, memo)
        elif diff < 0 and j < len(s2):
            memo[(i, j, diff)] = self.helper(s1, i, s2, j + 1, diff + 1, memo)
        
        return memo[(i, j, diff)]
    
    def getPossibleSizes(self, s):
        res = {int(s)}
        for i in range(1, len(s)):
            res |= {x + y for x in self.getPossibleSizes(s[:i]) for y in self.getPossibleSizes(s[i:])}
        return res