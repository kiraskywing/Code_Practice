class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        memo = collections.defaultdict(list)
        for a, b in edges:
            memo[a].append(b)
            memo[b].append(a)
        
        visited = {source}
        queue = collections.deque([source])
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == destination:
                    return True

                for nxt in memo[cur]:
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)
        
        return n == 1 and source == destination
