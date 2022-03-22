class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        memo = {c:i for i, c in enumerate(s)}
        res = []
        left, right = 0, 0
        for i, c in enumerate(s):
            right = max(right, memo[c])
            if i == right:
                res.append(right - left + 1)
                left = i + 1
        return res