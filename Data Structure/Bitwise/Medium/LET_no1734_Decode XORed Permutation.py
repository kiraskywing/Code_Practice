class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        start = 0
        for num in (encoded[::-2] + list(range(1, len(encoded) + 2))):
            start ^= num
        res = [start]
        for num in encoded:
            res.append(res[-1] ^ num)
        return res