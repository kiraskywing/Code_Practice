class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        word_dict = collections.defaultdict(list)
        for w in words:
            word_dict[w[0]].append(w)
        res = 0
        
        for c in s:
            temp = word_dict[c]
            word_dict[c] = []
            for w in temp:
                if len(w) == 1:
                    res += 1
                else:
                    word_dict[w[1]].append(w[1:])
        
        return res