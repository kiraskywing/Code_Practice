class Solution:
    def expand(self, s: str) -> List[str]:
        res = []
        self.dfs(s, 0, [], res)
        return sorted(res)
    
    def dfs(self, s, i, temp, res):
        if i == len(s):
            res.append(''.join(temp))
            return
        
        if s[i] == '{':
            j = i
            while s[j] != '}':
                j += 1
            for k in range(i + 1, j):
                if s[k].isalpha():
                    temp.append(s[k])
                    self.dfs(s, j + 1, temp, res)
                    temp.pop()
        
        elif s[i].isalpha():
            temp.append(s[i])
            self.dfs(s, i + 1, temp, res)
            temp.pop()
        else:
            self.dfs(s, i + 1, temp, res)