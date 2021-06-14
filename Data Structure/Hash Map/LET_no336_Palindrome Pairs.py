class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        words = {word:i for i, word in enumerate(words)}
        res = []
        for word in words:
            n = len(word)
            for i in range(n + 1):
                pre = word[:i]
                suf = word[i:]
                if pre == pre[::-1]:
                    front = suf[::-1]
                    if front != word and front in words:
                        res.append([words[front], words[word]])
                if i != n and suf == suf[::-1]:
                    back = pre[::-1]
                    if back != word and back in words:
                        res.append([words[word], words[back]])
        
        return res