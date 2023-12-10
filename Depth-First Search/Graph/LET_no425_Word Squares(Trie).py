class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.word_list = []
class Trie:
    def __init__(self, words):
        self.root = Node()
        for w in words:
            self.insert(w)
            
    def insert(self, w):
        cur = self.root
        for c in w:
            cur = cur.children[c]
            cur.word_list.append(w)
    
    def find(self, w):
        cur = self.root
        for c in w:
            if c not in cur.children:
                return None
            cur = cur.children[c]
        return cur
    
    def getWordsWithPrefix(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return []
            cur = cur.children[c]
        return cur.word_list

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        trie = Trie(words)
        res = []
        for w in words:
            self.dfs(trie, [w], res)
        return res
    
    def dfs(self, trie, temp, res):
        m, n = len(temp), len(temp[0])
        if m == n:
            res.append(temp[:])
            return
        
        prefix = ''.join(temp[i][m] for i in range(m))
        for w in trie.getWordsWithPrefix(prefix):
            if self.valid(trie, w, temp):
                temp.append(w)
                self.dfs(trie, temp, res)
                temp.pop()
                
    def valid(self, trie, w, temp):
        m, n = len(temp), len(temp[0])
        for j in range(m + 1, n):
            prefix = ''.join(temp[i][j] for i in range(m))
            prefix += w[j]
            if not trie.find(prefix):
                return False
        return True