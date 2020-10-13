"""
Definition for Undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: s: Undirected graph node
    @param: t: Undirected graph nodes
    @return: an integer
    """

    def sixDegrees(self, graph, s, t):
        if s == t:
            return 0

        queue = collections.deque([s])
        visited = {s}
        steps = 0

        while queue:
            steps += 1
            for i in range(len(queue)):
                node = queue.popleft()
                for friend in node.neighbors:
                    if friend == t:
                        return steps
                    if friend not in visited:
                        visited.add(friend)
                        queue.append(friend)

        return -1
