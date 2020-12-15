class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        values = sorted(zip(aliceValues, bobValues), key=sum, reverse=True)
        temp = sum(a for a, b in values[::2]) - sum(b for a, b in values[1::2])
        
        if temp > 0: return 1
        if temp < 0: return -1
        return 0