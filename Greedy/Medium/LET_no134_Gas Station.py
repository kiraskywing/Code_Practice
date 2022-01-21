class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        diff = [gas[i] - cost[i] for i in range(n)]
        if sum(diff) < 0:
            return -1
        
        cur, start = 0, 0
        for i in range(n):
            cur += diff[i]
            if cur < 0:
                cur = 0
                start = i + 1
        return start