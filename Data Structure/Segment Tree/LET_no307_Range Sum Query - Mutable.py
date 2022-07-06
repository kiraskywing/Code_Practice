class Node:
    def __init__(self, i, j):
        self.i, self.j = i, j
        self.left = self.right = None
        self.val = 0

class SegTree:
    def __init__(self, nums):
        self.root = self.build(nums, 0, len(nums) - 1)
        
    def build(self, nums, i, j):
        if i == j:
            cur = Node(i, j)
            cur.val = nums[i]
            return cur
        
        mid = (i + j) // 2
        cur = Node(i, j)
        cur.left = self.build(nums, i, mid)
        cur.right = self.build(nums, mid + 1, j)
        cur.val = cur.left.val + cur.right.val
        return cur
    
    def update(self, node, idx, val):
        if node.i == node.j:
            node.val = val
            return 
        
        mid = (node.i + node.j) // 2
        if idx <= mid:
            self.update(node.left, idx, val)
        else:
            self.update(node.right, idx, val)
        node.val = node.left.val + node.right.val
        
    def query(self, node, i, j):
        if node.i == i and node.j == j:
            return node.val
        
        mid = (node.i + node.j) // 2
        if j <= mid:
            return self.query(node.left, i, j)
        if i >= mid + 1:
            return self.query(node.right, i, j)
        return self.query(node.left, i, mid) + self.query(node.right, mid + 1, j)

class NumArray:

    def __init__(self, nums: List[int]):
        self.seg = SegTree(nums)

    def update(self, index: int, val: int) -> None:
        self.seg.update(self.seg.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.seg.query(self.seg.root, left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)