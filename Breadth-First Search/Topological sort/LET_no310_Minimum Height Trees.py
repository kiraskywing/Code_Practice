class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        connections = [set() for _ in range(n)]
        for a, b in edges:
            connections[a].add(b)
            connections[b].add(a)
        
        leaves = [i for i in range(n) if len(connections[i]) == 1]
        while n > 2:
            n -= len(leaves)
            next_leaves = []
            for i in leaves:
                j = connections[i].pop()
                connections[j].remove(i)
                if len(connections[j]) == 1:
                    next_leaves.append(j)
            leaves = next_leaves
        
        return leaves