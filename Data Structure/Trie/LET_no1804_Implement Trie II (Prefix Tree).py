class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.count = 0
        self.start_with = 0

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        cur.start_with += 1
        for c in word:
            cur = cur.children[c]
            cur.start_with += 1
        cur.count += 1

    def countWordsEqualTo(self, word: str) -> int:
        cur = self.root
        for c in word:
            if c not in cur.children or cur.start_with == 0:
                return 0
            cur = cur.children[c]
        return cur.count

    def countWordsStartingWith(self, prefix: str) -> int:
        cur = self.root
        for c in prefix:
            if c not in cur.children or cur.start_with == 0:
                return 0
            cur = cur.children[c]
        return cur.start_with

    def erase(self, word: str) -> None:
        cur = self.root
        cur.start_with -= 1
        for c in word:
            cur = cur.children[c]
            cur.start_with -= 1
        cur.count -= 1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)