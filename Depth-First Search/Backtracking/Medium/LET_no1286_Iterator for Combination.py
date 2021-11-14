class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.s = characters
        self.idx = [i for i in range(combinationLength)]

    def next(self) -> str:
        res = ""
        for i in self.idx:
            res += self.s[i]
        
        self.idx[-1] += 1
        if self.idx[-1] < len(self.s):
            return res
        
        i, remain = len(self.idx) - 2, 2
        while i >= 0:
            if self.idx[i] + remain < len(self.s):
                self.idx[i] += 1
                for j in range(i + 1, len(self.idx)):
                    self.idx[j] = self.idx[j - 1] + 1
                return res
            i -= 1
            remain += 1
        
        self.idx[0] = -1
        return res

    def hasNext(self) -> bool:
        return self.idx[0] != -1


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()