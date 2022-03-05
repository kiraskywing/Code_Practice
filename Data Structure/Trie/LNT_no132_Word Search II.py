# The same as LeetCode no212. Word Search II

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False
class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for w in words:
            self.insert(w)
    def insert(self, word):
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.is_word = True
    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.is_word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        trie = Trie(words)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, trie.root, [], res)
        return res
    
    def dfs(self, board, i, j, cur, temp, res):
        if cur.is_word:
            res.append(''.join(temp))
            cur.is_word = False
        if not (0 <= i < len(board) and 0 <= j < len(board[0])):
            return
        c = board[i][j]
        
        if c not in cur.children:
            return
        cur = cur.children[c]
        temp.append(c)
        board[i][j] = '*'
        self.dfs(board, i + 1, j, cur, temp, res)
        self.dfs(board, i - 1, j, cur, temp, res)
        self.dfs(board, i, j + 1, cur, temp, res)
        self.dfs(board, i, j - 1, cur, temp, res)
        board[i][j] = c
        temp.pop()