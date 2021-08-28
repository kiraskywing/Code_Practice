class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def issubsequence(sub, target):
            it  = iter(target)
            return all(c in it for c in sub)
        
        for sub in sorted(strs, key=len, reverse=True):
            if sum(issubsequence(sub, target) for target in strs) == 1:
                return len(sub)
        
        return -1