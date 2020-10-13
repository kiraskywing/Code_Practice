class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.build_graph(equations, values)
        return [self.find_path(graph, q) for q in queries]
    
    def build_graph(self, equations, values):
        graph = collections.defaultdict(list)
        for vertices, value in zip(equations, values):
            a, b = vertices
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))
        return graph
    
    def find_path(self, graph, query):
        m, n = query
        
        if m not in graph or n not in graph:
            return -1.0
        
        queue = collections.deque([(m, 1.0)])
        visited = set()
        
        while queue:
            front, cur_product = queue.popleft()
            if front == n:
                graph[m].append((n, cur_product))
                return cur_product
            visited.add(front)
            for neighbor, value in graph[front]:
                if neighbor not in visited:
                    queue.append((neighbor, cur_product * value))
        return -1
        