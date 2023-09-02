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

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie(dictionary)
        n = len(s)
        dp = [float('inf') for _ in range(n + 1)]
        dp[-1] = 0    # No extra character for an empty string

        for start in reversed(range(n)):
            dp[start] = dp[start + 1] + 1    # Initialize with worst-case scenario
            cur = trie.root
            for end in range(start, n):
                c = s[end]
                if c not in cur.children:
                    break
                cur = cur.children[c]
                if cur.is_word:
                    dp[start] = min(dp[start], dp[end + 1])

        return dp[0]