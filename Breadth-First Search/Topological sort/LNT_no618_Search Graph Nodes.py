"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """

    def searchNode(self, graph, values, node, target):
        if values[node] == target:
            return node

        queue = collections.deque([node])
        while queue:
            head = queue.popleft()
            for node in head.neighbors:
                if node in values:
                    if values[node] == target:
                        return node
                    queue.append(node)

        return None
