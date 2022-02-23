# The same as Leetcode no.133 Clone graph

"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """

    def cloneGraph(self, node):

        if not node:
            return node

        root = node

        nodes = self.get_nodes(node)

        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)

        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)

        return mapping[root]

    def get_nodes(self, node):
        q = collections.deque([node])
        result = set([node])

        while q:
            head = q.popleft()
            for neighbor in head.neighbors:
                if neighbor not in result:
                    result.add(neighbor)
                    q.append(neighbor)

        return result


class Solution2:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        memo = {node:Node(node.val)}
        queue = collections.deque([node])
        while queue:
            cur = queue.popleft()
            for nei in cur.neighbors:
                if nei not in memo:
                    memo[nei] = Node(nei.val)
                    queue.append(nei)
                memo[cur].neighbors.append(memo[nei])
        
        return memo[node]