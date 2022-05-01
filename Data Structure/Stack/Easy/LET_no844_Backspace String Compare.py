class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1, s2 = [], []
        self.helper(s, s1)
        self.helper(t, s2)
        return s1 == s2
    
    def helper(self, string, stack):
        for c in string:
            if c != '#':
                stack.append(c)
            elif stack:
                stack.pop()