"""
Definition of TrieNode:
class TrieNode:
    def __init__(self):
        # <key, value>: <Character, TrieNode>
        self.children = collections.OrderedDict()
        self.top10 = []
"""
class TrieService:

    def __init__(self):
        self.root = TrieNode()

    def get_root(self):
        # Return root of trie root, and 
        # lintcode will print the tree struct.
        return self.root

    # @param {str} word a string
    # @param {int} frequency an integer
    # @return nothing
    def insert(self, word, frequency):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.top10.append(frequency)
            
            cur.top10.append(frequency)
            cur.top10.sort(reverse=True)
            if len(cur.top10) > 10:
                cur.top10.pop()
