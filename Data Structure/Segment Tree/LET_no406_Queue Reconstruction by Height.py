class Node:
    def __init__(self, low, high):
        self.val = 1
        self.low, self.high = low, high
        self.left = self.right = None

class SegTree:
    def __init__(self, n):
        self.root = self.build(0, n - 1)
        
    def build(self, low, high):
        if low == high:
            return Node(low, high)
        
        mid = (low + high) // 2
        cur = Node(low, high)
        cur.left = self.build(low, mid)
        cur.right = self.build(mid + 1, high)
        cur.val = cur.left.val + cur.right.val
        
        return cur
    
    def query(self, node, k):
        if node.low == node.high:
            node.val = 0
            return node.low
        
        res = None
        if node.left.val >= k:
            res = self.query(node.left, k)
        else:
            res = self.query(node.right, k - node.left.val)
        node.val = node.left.val + node.right.val
        
        return res

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (x[0], -x[1]))
        seg = SegTree(len(people))
        res = [None] * len(people)
        
        for h, k in people:
            idx = seg.query(seg.root, k + 1)
            res[idx] = [h, k]
        
        return res

class Solution2:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (x[0], -x[1]))
        n = len(people)
        res = [None] * n
        
        for h, k in people:
            count = 0
            for i in range(n):
                if res[i] is None:
                    count += 1
                    if count == k + 1:
                        res[i] = [h, k]
                        break
        
        return res

class Solution3:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res