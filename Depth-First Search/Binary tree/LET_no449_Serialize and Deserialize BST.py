# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # serialize: use preorder traversal to get a sequence of tree nodes
    #            => concatenate them as a string
    # deserialize: split the input string, put them into a queue with their original order.
    # BST: the value of left child should less than the value of root
    #      the value of right child should greater than the value of root
    # use a helper function to construct the tree recursively
    # arguments: node, the lower bound value, the upper bound value
    # If the value at the front of queue is within the bound range, construct the node
    # left child => current value as upper bound, right child => current value as upper bound
    
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
        
        res = []
        self.preorder(root, res)    # Time & Space: O(n)
        return ' '.join(str(num) for num in res)
    
    def preorder(self, root, res):
        if not root:
            return 
        
        res.append(root.val)
        self.preorder(root.left, res)
        self.preorder(root.right, res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        
        queue = collections.deque([int(num) for num in data.split(' ')])
        # Time & Space: O(n)
        return self.construct_tree(queue, float('-inf'), float('inf'))
    
    def construct_tree(self, queue, min_val, max_val):
        if len(queue) == 0 or not (min_val < queue[0] < max_val):
            return None
        
        val = queue.popleft()
        cur = TreeNode(val)
        cur.left = self.construct_tree(queue, min_val, val)
        cur.right = self.construct_tree(queue, val, max_val)
        
        return cur

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans