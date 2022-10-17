class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # n equations and m queries
        graph = self.build_graph(equations, values)
        return [self.get_query_result(graph, q) for q in queries]    # Time: O(m * n)
        
    def build_graph(self, equations, values):    # Time & Space: O(n)
        graph = collections.defaultdict(list)
        for eq, val in zip(equations, values):
            a, b = eq
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))
        
        return graph
    
    def get_query_result(self, graph, query):
        a, b = query    
        if a not in graph:
            return -1.0
        if a == b:
            return 1.0

        queue = collections.deque([])
        visited = set()    # Space: O(n)
        
        for next_item, val in graph[a]:
            visited.add(next_item)
            queue.append((next_item, val))

        while queue:    # Time: O(n)
            item, cur = queue.popleft()
            if item == b:
                graph[a].append((b, cur))
                return cur

            for next_item, next_val in graph[item]:
                if next_item not in visited:
                    visited.add(next_item)
                    queue.append((next_item, cur * next_val))
        
        return -1.0
        
"""
# Example 1:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

# Example 2:
Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
"""