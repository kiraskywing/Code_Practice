class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        for i in range(len(capacity)):
            capacity[i] -= rocks[i]
        
        capacity.sort()
        res = 0
        for num in capacity:
            additionalRocks -= num
            if additionalRocks >= 0:
                res += 1
        return res