class Node:
    def __init__(self, lower, upper, val):
        self.lower, self.upper, self.val = lower, upper, val
        self.left, self.right = None, None

class CountIntervals:

    def __init__(self):
        self.root = Node(0, 10 ** 9, 0)

    def setRange(self, node, left, right):
        if left <= node.lower and node.upper <= right:
            node.val = node.upper - node.lower + 1
            node.left = node.right = None
            return
        
        mid = (node.upper + node.lower) // 2
        if not node.left and not node.right:
            node.left = Node(node.lower, mid, mid - node.lower + 1 if node.val else 0)
            node.right = Node(mid + 1, node.upper, node.upper - (mid + 1) + 1 if node.val else 0)
        if left <= mid:
            self.setRange(node.left, left, right)
        if right > mid:
            self.setRange(node.right, left, right)
        node.val = node.left.val + node.right.val
    
    def add(self, left: int, right: int) -> None:
        self.setRange(self.root, left, right)

    def count(self) -> int:
        return self.root.val


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()