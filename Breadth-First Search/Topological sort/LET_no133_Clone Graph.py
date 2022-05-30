class Solution:
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