# The same as LeetCode no425. Word Squares

class Solution:
    """
    @param: words: a set of words without duplicates
    @return: all word squares
    """

    def wordSquares(self, words):
        trie = Trie(words)

        result = []
        for word in words:
            self.dfs(trie, [word], result)
        return result

    def dfs(self, trie, square, result):
        rows = len(square)
        cols = len(square[0])
        if rows == cols:
            result.append(square[:])
            return

        prefix = ''.join(square[i][rows] for i in range(rows))
        for word in trie.get_words_with_prefix(prefix):
            if not self.checkPrefix(word, trie, square):
                continue
            square.append(word)
            self.dfs(trie, square, result)
            square.pop()

    def checkPrefix(self, word, trie, square):
        rows = len(square)
        cols = len(square[0])
        for j in range(rows + 1, cols):
            prefix = ''.join(square[i][j] for i in range(rows))
            prefix += word[j]
            if trie.find(prefix) is None:
                return False
        return True


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word_list = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
            node.word_list.append(word)

    def find(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return None
            node = node.children[c]
        return node

    def get_words_with_prefix(self, prefix):
        node = self.find(prefix)
        return [] if node is None else node.word_list