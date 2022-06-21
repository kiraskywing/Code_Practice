# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        
        res = []
        queue = collections.deque([root])
        while queue:
            cur = queue.popleft()
            res.append(str(cur.val) if cur else '#')
            if cur:
                queue.append(cur.left)
                queue.append(cur.right)
        
        return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        nodes = [TreeNode(int(val)) if val != '#' else None for val in data.split()]
        
        cur, fast = 0, 1
        while fast < len(nodes):
            while not nodes[cur]:
                cur += 1
            left, right = fast, fast + 1
            nodes[cur].left = nodes[left]
            nodes[cur].right = nodes[right]
            cur, fast = cur + 1, fast + 2
        
        return nodes[0]
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))