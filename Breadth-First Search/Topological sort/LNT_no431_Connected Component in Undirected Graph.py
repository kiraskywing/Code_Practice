"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    @return {int[][]} a connected set of a undirected graph
    """

    def connectedSet(self, nodes):

        visited = {node: False for node in nodes}
        result = []

        for node in nodes:
            if visited[node] == False:
                result.append(self.bfs(node, visited))

        return result

    def bfs(self, node, visited):
        temp = []
        queue = collections.deque([node])
        visited[node] = True

        while queue:
            cur = queue.popleft()
            temp.append(cur.label)
            for neighbor in cur.neighbors:
                if visited[neighbor] == False:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return sorted(temp)
