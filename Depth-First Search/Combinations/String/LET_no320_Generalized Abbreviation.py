class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        res = []
        self.dfs(word, 0, False, [], res)
        return res
    
    def dfs(self, w, start, prev_is_num, temp, res):
        if start == len(w):
            res.append(''.join(temp))
            return
        
        for size in range(1, len(w) - start + 1):
            if start == 0 or not prev_is_num:
                temp.append(str(size))
                self.dfs(w, start + size, True, temp, res)
                temp.pop()
            if start == 0 or prev_is_num:
                temp.append(w[start:start+size])
                self.dfs(w, start + size, False, temp, res)
                temp.pop()