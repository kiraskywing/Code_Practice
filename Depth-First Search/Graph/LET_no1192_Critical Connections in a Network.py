class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph, edges = self.buildGraph(connections)
        rank = [-2] * n
        self.dfs(0, 0, n, graph, edges, rank)
        return list(edges)
        
    def buildGraph(self, connections):
        graph = collections.defaultdict(list)
        edges = set()
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
            edges.add(tuple(sorted((a, b))))
        return graph, edges
    
    def dfs(self, cur, depth, max_depth, graph, edges, rank):
        if rank[cur] >= 0:
            return rank[cur]
        
        rank[cur] = depth
        min_back_depth = max_depth
        
        for nei in graph[cur]:
            if rank[nei] == depth - 1:
                continue    # don't immmediately go back to parent.
            back_depth = self.dfs(nei, depth + 1, max_depth, graph, edges, rank)
            if back_depth <= depth:
                edges.remove(tuple(sorted((cur, nei))))
            min_back_depth = min(min_back_depth, back_depth)
        
        return min_back_depth