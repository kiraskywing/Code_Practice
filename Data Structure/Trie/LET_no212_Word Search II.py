class Trie:
    def __init__(self, words):
        self.root = {}
        for w in words:
            self.insert(w)
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        trie = Trie(words)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie.root:
                    self.dfs(board, i, j, trie.root, res)
        return res
    
    def dfs(self, board, i, j, cur, res):
        c = board[i][j]
        nxt = cur[c]
        
        if '#' in nxt:
            res.append(nxt['#'])
            del nxt['#']
            
        board[i][j] = '*'
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            i2, j2 = i + di, j + dj
            if not (0 <= i2 < len(board) and 0 <= j2 < len(board[0])):
                continue
            if board[i2][j2] == '*' or board[i2][j2] not in nxt:
                continue
            self.dfs(board, i2, j2, nxt, res)
        board[i][j] = c
        
        if not cur[c]:
            del cur[c]