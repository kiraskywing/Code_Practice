class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        n = len(s)
        found = [False] * n
        for w in words:
            start = s.find(w)
            size = len(w)
            while start != -1:
                for i in range(start, start + size):
                    found[i] = True
                start = s.find(w, start + 1)
        
        res = []
        i = 0
        while i < n:
            if found[i]:
                res.append("<b>")
                j = i
                while j < n and found[j]:
                    j += 1
                res.append(s[i:j])
                res.append("</b>")
                i = j
            else:
                j = i
                while j < n and not found[j]:
                    j += 1
                res.append(s[i:j])
                i = j
        
        return ''.join(res)