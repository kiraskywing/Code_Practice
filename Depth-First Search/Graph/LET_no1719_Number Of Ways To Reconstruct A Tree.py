class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        for u, v in pairs:
            graph[u].add(v)
            graph[v].add(u)
        return self.helper(graph, set(graph.keys()))
    
    def helper(self, graph, nodes):
        table, n = collections.defaultdict(list), len(nodes) - 1
        for node in nodes:
            table[len(graph[node])].append(node)
        
        if len(table[n]) == 0:
            return 0
        
        root = table[n][0]
        
        for node in graph[root]:
            graph[node].remove(root)
        
        sub_graph, seen, i = collections.defaultdict(set), set(), 0
        
        for node in nodes:
            if node != root and node not in seen:
                self.dfs(graph, sub_graph, seen, i, node)
                i += 1
        
        cands = [self.helper(graph, sub_graph[node]) for node in sub_graph]
        if 0 in cands: return 0
        if 2 in cands: return 2
        if len(table[n]) >= 2: return 2
        return 1
    
    def dfs(self, graph, sub_graph, seen, i, node):
        sub_graph[i].add(node)
        seen.add(node)
        for nxt_node in graph[node]:
            if nxt_node not in seen:
                self.dfs(graph, sub_graph, seen, i, nxt_node)