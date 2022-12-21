class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        dislike_graph = collections.defaultdict(list)
        for a, b in dislikes:
            dislike_graph[a].append(b)
            dislike_graph[b].append(a)

        colors = [-1] * (n + 1)

        for i in range(1, n + 1):
            if colors[i] == -1 and not self.bfs(colors, dislike_graph, i):
                return False

        return True
    
    def bfs(self, colors, graph, start):
        queue = collections.deque([start])
        colors[start] = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                for nxt in graph[cur]:
                    if colors[nxt] == -1:
                        colors[nxt] = 1 - colors[cur]
                        queue.append(nxt)
                    elif colors[nxt] == colors[cur]:
                        return False
            
        return True