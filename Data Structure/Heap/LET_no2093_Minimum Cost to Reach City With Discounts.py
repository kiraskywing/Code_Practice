class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        graph = collections.defaultdict(list)
        for a, b, cost in highways:
            graph[a].append((b, cost))
            graph[b].append((a, cost))

        visited = dict()
        pq = [(0, 0, discounts)]
        while pq:
            cur_cost, cur, discounts = heapq.heappop(pq)
            
            if cur == n - 1:
                return cur_cost

            if cur in visited and discounts <= visited[cur]:
                continue
            visited[cur] = discounts
            
            for neighbor, cost in graph[cur]:
                if discounts > 0:
                    heapq.heappush(pq, (cur_cost + cost // 2, neighbor, discounts - 1))
                heapq.heappush(pq, (cur_cost + cost, neighbor, discounts))

        return -1