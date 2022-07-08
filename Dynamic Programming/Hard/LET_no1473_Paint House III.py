class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        prev, cur = {(0, 0): 0}, {}
        for i in range(m):
            for cc in (range(1, n + 1) if houses[i] == 0 else [houses[i]]):
                for pc, pb in prev:
                    cb = pb + int(pc != cc)
                    if cb > target:
                        continue
                    cur[(cc, cb)] = min(cur.get(((cc, cb)), float('inf')), prev[(pc, pb)] + (cost[i][cc - 1] if cc != houses[i] else 0))
            prev, cur = cur, {}
        
        return min([prev[pc, pb] for pc, pb in prev if pb == target] or [-1])