class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        pCounter = collections.Counter(p)
        sCounter = collections.Counter(s[: n - 1])
        res = []
        for i in range(n - 1, m):
            sCounter[s[i]] += 1
            if sCounter == pCounter:
                res.append(i - n + 1)
            back = s[i - n + 1]
            sCounter[back] -= 1
            if sCounter[back] == 0:
                del sCounter[back]
        return res