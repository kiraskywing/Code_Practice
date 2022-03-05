class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False
class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for w in words:
            self.insert(w)
    def insert(self, w):
        cur = self.root
        for c in w:
            cur = cur.children[c]
        cur.is_word = True

class Solution:
    """
    @param: board: a list of lists of character
    @param: words: a list of string
    @return: an integer
    """
    def boggleGame(self, board, words):
        trie = Trie(words)
        m, n = len(board), len(board[0])
        seen = [[0] * n for _ in range(m)]
        return self.dfs(0, 0, trie.root, m, n, board, seen)
        
    def dfs(self, start_i, start_j, node, m, n, board, seen):
        res = 0
        for i in range(start_i, m):
            for j in range(start_j, n):
                if seen[i][j]:
                    continue
                
                path = []
                visited = []
                
                self.getNxtWords(i, j, path, visited, node, board, seen, m, n)
                for p in path:
                    for px, py in p:
                        seen[px][py] = 1
                    
                    res = max(res, 1 + self.dfs(i, j + 1, node, m, n, board, seen))
                    
                    for px, py in p:
                        seen[px][py] = 0
            start_j = 0
        
        return res
            
    def getNxtWords(self, i, j, path, visited, node, board, seen, m, n):
        if seen[i][j]:
            return
        
        c = board[i][j]
        if c not in node.children:
            return
        
        node = node.children[c]
        if node.is_word:
            visited.append((i, j))
            path.append(list(visited))
            visited.pop()
            return
        
        seen[i][j] = 1
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            i2, j2 = i + di, j + dj
            if 0 <= i2 < m and 0 <= j2 < n:
                visited.append((i, j))
                self.getNxtWords(i2, j2, path, visited, node, board, seen, m, n)
                visited.pop()
        seen[i][j] = 0