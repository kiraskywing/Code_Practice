class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
            
        seen = set()
        queue = collections.deque()
        
        for start in graph:
            if len(graph[start]) == 1:
                queue.append(start)
                break
        
        res = []
        while queue:
            cur = queue.popleft()
            seen.add(cur)
            res.append(cur)
            for nxt in graph[cur]:
                if nxt not in seen:
                    queue.append(nxt)
        
        return res