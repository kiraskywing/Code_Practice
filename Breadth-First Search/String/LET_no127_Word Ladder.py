class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_memo = set(wordList)
        if endWord not in word_memo:
            return 0
        
        queue = collections.deque([beginWord])
        visited = set([beginWord])
        times = 1
        
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == endWord:
                    return times
                for nxt in self.get_next_words(cur, word_memo):
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)
            times += 1
        
        return 0
    
    def get_next_words(self, w, word_memo):
        res = []
        for i in range(len(w)):
            for d in range(26):
                c = chr(ord('a') + d)
                if c == w[i]:
                    continue
                nxt = w[:i] + c + w[i+1:]
                if nxt in word_memo:
                    res.append(nxt)
        
        return res