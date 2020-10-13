"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    def topSort(self, graph):

        node_of_indegree = self.get_indegree(graph)

        result = []
        q = collections.deque([])

        for node in graph:
            if node_of_indegree[node] == 0:
                q.append(node)

        while q:
            node = q.popleft()
            result.append(node)
            for neighbor in node.neighbors:
                node_of_indegree[neighbor] -= 1
                if node_of_indegree[neighbor] == 0:
                    q.append(neighbor)

        return result

    def get_indegree(self, graph):
        node_of_indegree = {x: 0 for x in graph}

        for node in graph:
            for neighbor in node.neighbors:
                node_of_indegree[neighbor] += 1

        return node_of_indegree