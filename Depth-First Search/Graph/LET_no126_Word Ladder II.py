class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordset = set(wordList)
        if endWord not in wordset:
            return []
        
        wordset.add(beginWord)
        distance = dict()
        self.getGraph(endWord, beginWord, wordset, distance)
        if beginWord not in distance:
            return []
        
        res = []
        self.searchAllPaths(distance, wordset, [beginWord], res)
        return res
    
    def getGraph(self, start, end, wordset, distance):
        distance[start] = 0
        queue = collections.deque([start])
        
        while queue:
            cur = queue.popleft()
            if end in distance and distance[cur] > distance[end]:
                continue
                
            for next_word in self.getNextWords(cur, wordset):
                if next_word not in distance:
                    distance[next_word] = distance[cur] + 1
                    queue.append(next_word)
    
    def getNextWords(self, w, wordset):
        res = []
        for i in range(len(w)):
            for d in range(26):
                c = chr(ord('a') + d)
                if c == w[i]:
                    continue
                cur = w[:i] + c + w[i+1:]
                if cur in wordset:
                    res.append(cur)
        return res
    
    def searchAllPaths(self, distance, wordset, temp, res):
        cur = temp[-1]
        if distance[cur] == 0:
            res.append(temp[:])
            return
        
        for next_word in self.getNextWords(cur, wordset):
            if next_word in distance and distance[next_word] == distance[cur] - 1:
                temp.append(next_word)
                self.searchAllPaths(distance, wordset, temp, res)
                temp.pop()