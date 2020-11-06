class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odds = sum(num % 2 for num in position)
        return min(odds, len(position) - odds)