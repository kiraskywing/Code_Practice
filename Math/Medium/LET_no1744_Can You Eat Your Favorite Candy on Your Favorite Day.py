class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        candiesCount = [0] + list(accumulate(candiesCount))
        return [candiesCount[t] // c <= d < candiesCount[t + 1] for t, d, c in queries]