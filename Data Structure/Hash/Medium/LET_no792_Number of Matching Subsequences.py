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

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        res = 0
        memo = [[] for _ in range(26)]
        for word in words:
            it = iter(word)
            memo[ord(next(it)) - ord('a')].append(it)
            
        for c in s:
            idx = ord(c) - ord('a')
            cur = memo[idx]
            memo[idx] = []
            for it in cur:
                nxt = next(it, None)
                if nxt:
                    memo[ord(nxt) - ord('a')].append(it)
                else:
                    res += 1
        
        return res