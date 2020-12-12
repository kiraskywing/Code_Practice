class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:

        memo = {}
        for word_a, word_b in synonyms:
            memo[word_a] = word_b
            memo[word_b] = word_a

        sym = {}
        self.bfs(memo, sym)

        S = text.split()
        result, cur = [], []
        self.dfs(memo, sym, S, 0, cur, result)
        return result

    def bfs(self, memo, sym):
        for word in memo:
            if word not in sym:
                bfs = [word]
                seen = set([word])
                for word in bfs:
                    if memo[word] not in seen:
                        bfs.append(memo[word])
                        seen.add(memo[word])
                bfs.sort()
                for word in bfs:
                    memo[word] = bfs[0]
                if bfs[0] not in sym:
                    sym[bfs[0]] = bfs

    def dfs(self, memo, sym, string, i, cur, result):
        if i == len(string):
            result.append(' '.join(cur))
            return

        first = memo.get(string[i], string[i])
        words = sym.get(first, [first])

        for w in words:
            cur.append(w)
            self.dfs(memo, sym, string, i + 1, cur, result)
            cur.pop()
