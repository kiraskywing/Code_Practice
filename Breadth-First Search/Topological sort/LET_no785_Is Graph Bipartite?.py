class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0] * n
        
        for i in range(n):
            if colors[i] != 0:
                continue
            queue = collections.deque([i])
            colors[i] = 1
            
            while queue:
                cur = queue.popleft()
                for nxt in graph[cur]:
                    if colors[nxt] == 0:
                        colors[nxt] = -colors[cur]
                        queue.append(nxt)
                    elif colors[nxt] != -colors[cur]:
                        return False
        
        return True