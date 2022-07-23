class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        memo = collections.defaultdict(list)
        for i, j in edges:
            memo[i].append(j)
        
        if len(memo[destination]) > 0:
            return False
        
        state = [0] * n    # 0: not visited, 1: visited but not to dest, 2: visited and to dest 
        return self.dfs(memo, source, destination, state)
    
    def dfs(self, edges, source, destination, state):
        if state[source] != 0:
            return state[source] == 2
        if not edges[source]:
            return source == destination
        
        state[source] = 1
        for nxt in edges[source]:
            if not self.dfs(edges, nxt, destination, state):
                return False
        state[source] = 2
        
        return True