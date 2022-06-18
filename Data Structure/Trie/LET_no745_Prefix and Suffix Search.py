class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.memo = set()
class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, w1, w2):
        cur = self.root
        for c in w1:
            cur = cur.children[c]
            cur.memo.add(w2)
    
    def find(self, s):
        cur = self.root
        for c in s:
            cur = cur.children[c]
            if not cur.memo:
                break
        return cur.memo
            

class WordFilter:

    def __init__(self, words: List[str]):
        self.word_index = {}
        self.prefix_trie = Trie()
        self.surfix_trie = Trie()
        for i, w in enumerate(words):
            self.word_index[w] = i
            self.prefix_trie.insert(w, w)
            self.surfix_trie.insert(w[::-1], w)

    def f(self, prefix: str, suffix: str) -> int:
        a = self.prefix_trie.find(prefix)
        b = self.surfix_trie.find(suffix[::-1])
        res = -1
        for w in a & b:
            res = max(res, self.word_index[w])
        return res


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)