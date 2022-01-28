class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in reversed(word):
            cur = cur.children[c]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        word = word[::-1]
        return self.helper(cur, word, 0)
    
    def helper(self, cur, word, i):
        if i == len(word):
            return cur.isEnd
        
        c = word[i]
        if c == '.':
            for c2 in cur.children:
                if self.helper(cur.children[c2], word, i + 1):
                    return True
            return False
        else:
            if c in cur.children:
                return self.helper(cur.children[c], word, i + 1)
            return False
                    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)