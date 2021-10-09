# The same as LeetCode no212. Word Search II

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.is_word = True
    def search(self, word):
        cur = self.root
        for c in word:
            cur = cur.children.get(c)
            if not cur:
                return False
        return cur.is_word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        trie = Trie()
        for w in words:
            trie.insert(w)
        root = trie.root
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, root, "", res)
        return res
    
    def dfs(self, board, i, j, cur, s, res):
        if cur.is_word:
            res.append(s)
            cur.is_word = False
        if not (0 <= i < len(board) and 0 <= j < len(board[0])):
            return
        temp = board[i][j]
        cur = cur.children.get(temp)
        if not cur:
            return
        board[i][j] = '*'
        self.dfs(board, i + 1, j, cur, s + temp, res)
        self.dfs(board, i - 1, j, cur, s + temp, res)
        self.dfs(board, i, j + 1, cur, s + temp, res)
        self.dfs(board, i, j - 1, cur, s + temp, res)
        board[i][j] = temp