class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.memo = collections.defaultdict(set)
        for w in dictionary:
            if len(w) <= 2:
                self.memo[w].add(w)
            else:
                self.memo[w[0] + str(len(w) - 2) + w[-1]].add(w)
        
    def isUnique(self, word: str) -> bool:
        key = ""
        if len(word) <= 2:
            key = word
        else:
            key = word[0] + str(len(word) - 2) + word[-1]
        
        if key not in self.memo:
            return True
        return len(self.memo[key]) == 1 and word in self.memo[key]


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)