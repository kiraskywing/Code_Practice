class ProcessNode:
    def __init__(self, val):
        self.val = val
        self.children = []

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        tree = dict()
        
        for child, parent in zip(pid, ppid):
            if child not in tree:
                tree[child] = ProcessNode(child)
            if parent != 0 and parent not in tree:
                tree[parent] = ProcessNode(parent)
                
            if parent != 0:
                tree[parent].children.append(tree[child])
            
        res = {kill}
        queue = collections.deque([kill])
        while queue:
            cur = queue.popleft()
            for nxt in tree[cur].children:
                if nxt.val not in res:
                    res.add(nxt.val)
                    queue.append(nxt.val)
        
        return list(res)