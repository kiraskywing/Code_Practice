# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # empty input? => No
        # go to the deepest level and get the leftmost node
        
        # Approach: use DFS
        # use "pos" to know the relative position at the level
        # a node without children (may be at the bottom level): return (level, node)
        # a node with children: search left and right child
        # compare order: first level then the leftmost node
        
        level, node = self.helper(root, 0)    # Time: O(n), Space (call stack): O(h) where h is the tree height
        return node.val
    
    def helper(self, root, level):
        if not root:
            return 0, None
        
        left_level, left_node = self.helper(root.left, level + 1)
        right_level, right_node = self.helper(root.right, level + 1)
        
        if left_node and right_node:            # left and right child exist
            if left_level < right_level:        # choose the deepest first
                return right_level, right_node  # then choose the leftmost
            return left_level, left_node
        
        if left_node:                           # either left or right child exist
            return left_level, left_node
        if right_node:
            return right_level, right_node
        
        return level, root                      # No left and right child

class Solution2:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # empty input? => no
        
        # Approach: recursive dfs
        # create gobal variables: res_node, depth, level_pos
        # To find: (1) the depthest node -> (2) the leftmost node
        # traverse all nodes => once find a node with (1) deeper depth -> (2) lefter pos
        #                    => update the res_node
        # helper funciont arguments: node, depth, pos
        
        self.res_depth, self.res_pos = 0, float('inf')
        self.res_node = None
        self.helper(root, 0, 0)   # Time: O(n), Space: O(h)
        return self.res_node.val
    
    def helper(self, root, depth, pos):
        if not root.left and not root.right:
            if depth > self.res_depth:
                self.res_depth, self.res_pos = depth, pos
                self.res_node = root
            elif depth == self.res_depth and pos < self.res_pos:
                self.res_pos = pos
                self.res_node = root
                
            return
        
        if root.left:
            self.helper(root.left, depth + 1, pos - 1)
        if root.right:
            self.helper(root.right, depth + 1, pos + 1)