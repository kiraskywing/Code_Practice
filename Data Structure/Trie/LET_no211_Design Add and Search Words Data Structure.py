class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.is_word = True

    def search(self, word: str) -> bool:
        return self.helper(self.root, word, 0)
    
    def helper(self, cur, word, i):
        if i == len(word):
            return cur.is_word
        
        c = word[i]
        if c == '.':
            for _, child in cur.children.items():
                if self.helper(child, word, i + 1):
                    return True
            return False
        else:
            if c not in cur.children:
                return False
            return self.helper(cur.children[c], word, i + 1)
                


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)