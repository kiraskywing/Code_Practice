class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        degree = [0 for _ in range(n)]
        neighbors = collections.defaultdict(list)
        for a, b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
            degree[a] += 1
            degree[b] += 1

        queue = collections.deque([i for i in range(n) if degree[i] == 1])
        res = None
        while queue:
            temp = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                temp.append(cur)
                for neighbor in neighbors[cur]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        queue.append(neighbor)
            res = temp
        
        return res
