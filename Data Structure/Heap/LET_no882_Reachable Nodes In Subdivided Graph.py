class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        e = collections.defaultdict(dict)
        for i, j, l in edges:
            e[i][j] = e[j][i] = l
        pq = [(-maxMoves, 0)]
        seen = {}
        
        while pq:
            moves, i = heapq.heappop(pq)
            if i not in seen:
                seen[i] = -moves
                for j in e[i]:
                    moves2 = -moves - e[i][j] - 1
                    if j not in seen and moves2 >= 0:
                        heapq.heappush(pq, (-moves2, j))
        
        res = len(seen)
        for i, j, l in edges:
            res += min(seen.get(i, 0) + seen.get(j, 0), l)
        return res