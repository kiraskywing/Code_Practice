# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        record = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        
        while queue:
            temp = collections.defaultdict(list)
            for _ in range(len(queue)):
                node, col = queue.popleft()
                if node.left:
                    queue.append((node.left, col - 1))
                if node.right:
                    queue.append((node.right, col + 1))
                temp[col].append(node.val)
            for key, value in temp.items():
                record[key].extend(sorted(value))
        
        return [record[key] for key in sorted(record)]