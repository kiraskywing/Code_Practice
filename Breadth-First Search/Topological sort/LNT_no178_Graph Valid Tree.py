# The same as LeetCode no261. Graph Valid Tree

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        # valid tree: 1. 連通性 2. n - 1 edges 3. no ring
        if n - 1 != len(edges):
            return False

        neighbors = collections.defaultdict(list)
        for start, end in edges:
            neighbors[start].append(end)
            neighbors[end].append(start)

        visited = {0}
        queue = collections.deque([0])

        while queue:
            node = queue.popleft()
            for child in neighbors[node]:
                if child not in visited:
                    visited.add(child)
                    queue.append(child)

        return len(visited) == n
