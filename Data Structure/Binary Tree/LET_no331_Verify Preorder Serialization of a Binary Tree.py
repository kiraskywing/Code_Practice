class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(',')
        slot = 1
        for node in nodes:
            if slot == 0:
                return False
            if node == '#':
                slot -= 1
            else:
                slot += 1
        return slot == 0

class Solution2:
    def isValidSerialization(self, preorder: str) -> bool:
        # empty input string? => no, minimum size = 1
        # possible input string is '#'
        
        # Approach: Queue + recursive DFS
        # split input string into numbers and '#', put them into queue
        # use helper function to construct the tree recursively and with preorder
        # preorder: construct current node -> construct left subtree -> construct right subtree
        # To construct current node: pop one string from queue
        # case1: queue is empty => the input is invalid, return False
        # case2: get number => construct node, check left subtree and right subtree
        #                      return true if both left and right are valid
        # case3: get '#' => construct null, return true
        # Notice: need to check the queue is empty after construction
        
        if preorder == '#':
            return True
        
        queue = collections.deque([s for s in preorder.split(',')])    # Space: O(n)
        return self.helper(queue) and len(queue) == 0   # Time: O(n), call stack: O(h)
    
    def helper(self, queue):
        if len(queue) == 0:
            return False
        
        s = queue.popleft()
        if s == '#':
            return True
        
        left_valid = self.helper(queue)
        right_valid = self.helper(queue)
        
        return left_valid and right_valid