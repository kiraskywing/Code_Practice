class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res, record = [], collections.Counter(s)
        for c in order:
            if c in record:
                res.append(c * record.pop(c))
        for c, n in record.items():
            res.append(c * n)
        return ''.join(res)