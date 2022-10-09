# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        record = set()
        queue = collections.deque([root])
        
        while queue:
            cur = queue.popleft()
            if k - cur.val in record:
                return True
            record.add(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        
        return False

class Solution2:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        inorder_list = []
        self.inorder_traversal(root, inorder_list)
        
        left, right = 0, len(inorder_list) - 1
        while left < right:
            cur = inorder_list[left] + inorder_list[right]
            if cur == k:
                return True
            elif cur < k:
                left += 1
            else:
                right -= 1
        
        return False
    
    def inorder_traversal(self, root, res):
        if not root:
            return 
        
        self.inorder_traversal(root.left, res)
        res.append(root.val)
        self.inorder_traversal(root.right, res)