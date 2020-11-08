class Solution:
    def balancedString(self, s: str) -> int:

        count = collections.Counter(s)

        i, res = 0, len(s)

        for index, char in enumerate(s):
            count[char] -= 1

            while i < len(s) and all(count[x] <= len(s) // 4 for x in "QWER"):
                res = min(res, index - i + 1)
                count[s[i]] += 1
                i += 1

        return res