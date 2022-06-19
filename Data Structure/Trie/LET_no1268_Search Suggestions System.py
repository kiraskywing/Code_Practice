class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.word_list = []
        
class Trie:
    def __init__(self, words):
        self.root = Node()
        for i, w in enumerate(words):
            self.insert(w, i)
    
    def insert(self, w, i):
        cur = self.root
        for c in w:
            cur = cur.children[c]
            cur.word_list.append(i)
    
    def find(self, prefix, words):
        res = []
        cur = self.root
        for c in prefix:
            cur = cur.children[c]
            res.append([words[cur.word_list[i]] for i in range(min(3, len(cur.word_list)))])
        return res

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie(products)
        return trie.find(searchWord, products)