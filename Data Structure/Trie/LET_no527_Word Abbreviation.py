class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.count = 0

class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, w):
        cur = self.root
        for c in w:
            cur.count += 1
            cur = cur.children[c]
            
    def find(self, w):
        cur = self.root
        for i, c in enumerate(w):
            if cur.count == 1:
                return i
            cur = cur.children[c]
            
        return len(w)

class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        groups = collections.defaultdict(list)
        for index, w in enumerate(words):
            groups[(len(w), w[0], w[-1])].append((w, index))
            
        res = [None] * len(words)
        for wordset in groups.values():
            trie = Trie()
            for w, _ in wordset:
                trie.insert(w[1:])
            
            for w, index in wordset:
                i = trie.find(w[1:]) + 1
                if len(w) - (i + 1) > 1:
                    res[index] = w[:i] + str(len(w) - (i + 1)) + w[-1]
                else:
                    res[index] = w
        
        return res