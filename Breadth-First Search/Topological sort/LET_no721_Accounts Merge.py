class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = dict()
        email_to_name = dict()
        
        for acc in accounts:
            name = acc[0]
            for i, email in enumerate(acc[1:], 1):
                email_to_name[email] = name
                if email not in graph:
                    graph[email] = []
                if i > 1:
                    prev_email = acc[i - 1]
                    graph[email].append(prev_email)
                    graph[prev_email].append(email)
                    
        
        res = []
        visited = set()
        for email in graph:
            if email not in visited:
                visited.add(email)
                res.append([email_to_name[email]] + self.bfs(email, graph, visited))
        return res
    
    def bfs(self, start, graph, visited):
        res = []
        queue = collections.deque([start])
        while queue:
            cur = queue.popleft()
            res.append(cur)
            for nxt in graph[cur]:
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)
        
        return sorted(res)