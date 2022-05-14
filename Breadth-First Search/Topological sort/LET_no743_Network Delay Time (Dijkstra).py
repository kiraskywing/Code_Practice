class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        vertex_weight = [float('inf')] * n
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u - 1].append((v - 1, w))
        
        vertex_weight[k - 1] = 0
        heap =[]
        heapq.heappush(heap, (0, k - 1))
        
        while heap:
            total, cur_node = heapq.heappop(heap)
            for next_node, w in edges[cur_node]:
                if vertex_weight[cur_node] + w < vertex_weight[next_node]:
                    vertex_weight[next_node] = vertex_weight[cur_node] + w
                    heapq.heappush(heap, (vertex_weight[next_node], next_node))
        
        res = max(vertex_weight)
        return res if res != float('inf') else -1