class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.size = 0
class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, w, n):
        cur = self.root
        for c in w:
            cur = cur.children[c]
        cur.size += n
        return cur

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()
        temp = []
        for w in set(words):
            temp.append(trie.insert(w[::-1], len(w)))
        
        return sum(node.size + 1 for node in temp if not node.children)