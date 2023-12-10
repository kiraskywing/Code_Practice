class Solution:
    """
    @param: words: a set of words without duplicates
    @return: all word squares
    """

    def wordSquares(self, words):
        ans = []
        if not words:
            return ans

        prefixHash = self.getPrefixHash(words)
        self.dfs(0, len(words[0]), prefixHash, [], ans)
        return ans

    def getPrefixHash(self, words):
        result = collections.defaultdict(list)

        for word in words:
            result[''].append(word)
            prefix = ''
            for c in word:
                prefix += c
                result[prefix].append(word)

        return result

    def dfs(self, index, wordLen, prefixHash, square, ans):
        if index == wordLen:
            ans.append(square[:])
            return

        prefix = ''
        for i in range(index):
            prefix += square[i][index]

        for word in prefixHash[prefix]:
            if not self.checkPrefix(index, word, wordLen, prefixHash, square):
                continue
            square.append(word)
            self.dfs(index + 1, wordLen, prefixHash, square, ans)
            square.pop()

    def checkPrefix(self, index, word, wordLen, prefixHash, square):
        for i in range(index + 1, wordLen):
            prefix = ''
            for j in range(index):
                prefix += square[j][i]
            prefix += word[i]

            if prefix not in prefixHash:
                return False
        return True
