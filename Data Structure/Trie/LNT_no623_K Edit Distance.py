from typing import (
    List,
)

class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.is_word = False
        self.word = ""
class Trie:
    def __init__(self, words):
        self.root = Node()
        for w in words:
            self.insert(w)
    def insert(self, w):
        cur = self.root
        for c in w:
            cur = cur.children[c]
        cur.is_word = True
        cur.word = w

class Solution:
    """
    @param words: a set of stirngs
    @param target: a target string
    @param k: An integer
    @return: output all the strings that meet the requirements
    """
    def k_distance(self, words: List[str], target: str, k: int) -> List[str]:
        trie = Trie(words)
        n = len(target)
        dp = [i for i in range(n + 1)]
        res = []
        self.dfs(trie.root, target, n, k, dp, res)
        return res

    def dfs(self, cur, target, n, k, dp, res):
        if cur.is_word and dp[n] <= k:
            res.append(cur.word)

        next_dp = [0 for _ in range(n + 1)]
        next_dp[0] = dp[0] + 1
        for c in cur.children:
            for i in range(1, n + 1):
                if target[i - 1] == c:
                    next_dp[i] = min(dp[i - 1], dp[i] + 1, next_dp[i - 1] + 1)
                else:
                    next_dp[i] = min(dp[i - 1] + 1, dp[i] + 1, next_dp[i - 1] + 1)
        
            self.dfs(cur.children[c], target, n, k, next_dp, res)

