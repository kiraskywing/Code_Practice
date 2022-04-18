class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        children = [[] for _ in range(len(s))]
        for i, p in enumerate(parent):
            if p >= 0:
                children[p].append(i)
            
        self.res = 0
        self.helper(children, 0, s)
        return self.res
    
    def helper(self, children, cur, s):
        temp = [0, 0]
        for child in children[cur]:
            length = self.helper(children, child, s)
            if s[child] != s[cur]:
                temp.append(length)
        
        temp.sort(reverse=True)
        self.res = max(self.res, 1 + sum(temp[:2]))
        return 1 + temp[0]
        