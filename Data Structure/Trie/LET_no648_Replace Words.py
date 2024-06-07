class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.word = None

class Trie:
    def __init__(self, words):
        self.root = Node()
        for word in words:
            self.insert(word)

    def insert(self, word):
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.word = word

    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return word
            cur = cur.children[c]
            if cur.word is not None:
                return cur.word
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie(dictionary)
        word_list = sentence.split()
        res = []
        for word in word_list:
            res.append(trie.search(word))
        
        return ' '.join(res)