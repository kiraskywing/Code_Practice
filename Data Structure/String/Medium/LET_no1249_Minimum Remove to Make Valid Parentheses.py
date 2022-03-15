class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        removes = set()
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    removes.add(i)
        
        for i in stack:
            removes.add(i)
            
        return ''.join(c for i, c in enumerate(s) if i not in removes)