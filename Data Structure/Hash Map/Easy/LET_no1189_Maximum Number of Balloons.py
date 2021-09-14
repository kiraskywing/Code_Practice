class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        record = collections.Counter(text)
        letters = [('b', 1), ('a', 1), ('l', 2), ('o', 2), ('n', 1)]
        res = len(text) // len("balloon")
        for c, n in letters:
            res = min(res, record[c] // n)
        return res