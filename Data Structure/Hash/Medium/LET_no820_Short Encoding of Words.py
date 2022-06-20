class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        word_set = set(words)
        for w in words:
            for i in range(1, len(w)):
                word_set.discard(w[i:])
                
        return sum(len(w) for w in word_set) + len(word_set)