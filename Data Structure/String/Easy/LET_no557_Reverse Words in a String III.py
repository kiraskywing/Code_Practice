class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        for w in s.split():
            res.append(''.join(list(w)[::-1]))
        return ' '.join(res)