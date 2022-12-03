class Solution:
    def frequencySort(self, s: str) -> str:
        memo = collections.Counter(s)
        pairs = [(c, val) for c, val in memo.items()]
        pairs.sort(key=lambda x : -x[1])
        return ''.join(c * val for c, val in pairs)