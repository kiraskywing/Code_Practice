"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        if not root:
            return 0
        
        cur_max, res_max = self.helper(root)
        return res_max
    
    def helper(self, node):
        cur_largest = cur_second = res = 0
        
        for node2 in node.children:
            nxt_largest, nxt_res = self.helper(node2)
            if nxt_largest > cur_largest:
                cur_largest, cur_second = nxt_largest, cur_largest
            elif nxt_largest > cur_second:
                cur_second = nxt_largest
            res = max(res, nxt_res)
        
        res = max(res, cur_largest + cur_second)
        return cur_largest + 1, res