class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for w in words:
            if len(w) != len(pattern): continue
            w2p, p2w = dict(), dict()
            valid = True
            for i, j in zip(w, pattern):
                if i not in w2p and j not in p2w:
                    w2p[i] = j
                    p2w[j] = i
                else:
                    if i in w2p and w2p[i] != j or j in p2w and p2w[j] != i: 
                        valid = False
                        break
            if valid: res.append(w)
        
        return res