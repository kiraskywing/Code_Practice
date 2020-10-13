class Solution:
    """
    @param: words: a set of words without duplicates
    @return: all word squares
    """

    def wordSquares(self, words):
        trie = Trie()
        for word in words:
            trie.add(word)

        result = []
        for word in words:
            self.dfs(trie, [word], result)
        return result

    def dfs(self, trie, square, result):
        index = len(square)
        wordLen = len(square[0])
        if index == wordLen:
            result.append(square[:])
            return

        prefix = ''.join(square[i][index] for i in range(index))
        for word in trie.get_words_with_prefix(prefix):
            if not self.checkPrefix(word, trie, square):
                continue
            square.append(word)
            self.dfs(trie, square, result)
            square.pop()

    def checkPrefix(self, word, trie, square):
        index = len(square)
        wordLen = len(square[0])
        for i in range(index + 1, wordLen):
            prefix = ''.join(square[j][i] for j in range(index))
            prefix += word[i]
            if trie.find(prefix) is None:
                return False
        return True


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word_list = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.word_list.append(word)
        node.is_word = True

    def find(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                return None
        return node

    def get_words_with_prefix(self, prefix):
        node = self.find(prefix)
        return [] if node is None else node.word_list

    def contains(self, word):
        node = self.find(word)
        return node is not None and node.is_word