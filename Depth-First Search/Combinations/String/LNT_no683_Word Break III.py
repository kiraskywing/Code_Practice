class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        max_len, new_dict = self.initialize(dict)
        return self.memo_search(s.lower(), 0, max_len, new_dict, {})

    def initialize(self, words):
        max_len, result = -sys.maxsize, set()
        for word in words:
            max_len = max(max_len, len(word))
            result.add(word.lower())
        return max_len, result

    def memo_search(self, string, index, max_len, words, memo):
        if index == len(string):
            return 1
        if index in memo:
            return memo[index]

        memo[index] = 0
        for i in range(index, len(string)):
            if i - index + 1 > max_len:
                break
            word = string[index: i + 1]
            if word not in words:
                continue

            memo[index] += self.memo_search(string, i + 1, max_len, words, memo)

        return memo[index]