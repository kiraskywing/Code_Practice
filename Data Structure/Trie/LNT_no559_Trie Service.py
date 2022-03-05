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
            
            n = len(cur.top10)
            i = n - 1
            while i > 0 and cur.top10[i - 1] < frequency:
                cur.top10[i] = cur.top10[i - 1]
                i -= 1
            cur.top10[i] = frequency
            if n > 10:
                cur.top10.pop()
