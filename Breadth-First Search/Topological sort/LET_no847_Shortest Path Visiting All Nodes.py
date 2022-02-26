class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        all_visited = (1 << n) - 1
        start_nodes = [(i, 1 << i) for i in range(n)]
        seen = set(start_nodes)
        queue = collections.deque(start_nodes)
        steps = 0
        while queue:
            for _ in range(len(queue)):
                cur, visited = queue.popleft()
                if visited == all_visited:
                    return steps
                for neighbor in graph[cur]:
                    next_pair = (neighbor, visited | 1 << neighbor)
                    if next_pair not in seen:
                        seen.add(next_pair)
                        queue.append(next_pair)
            steps += 1
            
        return -1