class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        wTable = collections.defaultdict(int)
        for w in words:
            wTable[self.getMask(w)] += 1
        
        res = [0] * len(puzzles)
        for i in range(len(puzzles)):
            subMask = mask = self.getMask(puzzles[i])
            firstChar = ord(puzzles[i][0]) - ord('a')
            
            while subMask:
                if subMask >> firstChar & 1:
                    res[i] += wTable[subMask]
                subMask = (subMask - 1) & mask
        
        return res
    
    def getMask(self, w):
        res = 0
        for c in w:
            res |= (1 << (ord(c) - ord('a')))
        return res