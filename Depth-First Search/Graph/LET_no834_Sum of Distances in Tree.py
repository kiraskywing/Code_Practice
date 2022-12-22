class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = collections.defaultdict(set)
        for a, b in edges:
            tree[a].add(b)
            tree[b].add(a)

        res = [0] * n
        count = [1] * n

        self.post_order_traversal(tree, res, count, 0, -1)
        self.pre_order_traversal(tree, res, count, 0, -1)

        return res

    def post_order_traversal(self, tree, res, count, cur, pre):
        for nxt in tree[cur]:
            if nxt != pre:
                self.post_order_traversal(tree, res, count, nxt, cur)
                count[cur] += count[nxt]
                res[cur] += res[nxt] + count[nxt]

    def pre_order_traversal(self, tree, res, count, cur, pre):
        n = len(count)
        for nxt in tree[cur]:
            if nxt != pre:
                res[nxt] = res[cur] - count[nxt] + n - count[nxt]
                self.pre_order_traversal(tree, res, count, nxt, cur)