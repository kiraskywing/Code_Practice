class Node:
    def __init__(self, val):
        self.val = val
        self.prev = self.next = None

class MaxStack:

    def __init__(self):
        self.dummy = Node(-1)
        self.dummy.next = self.dummy.prev = self.dummy
        self.heap = []
        self.val_to_node = collections.defaultdict(list)

    def push(self, x: int) -> None:
        cur = Node(x)
        tail = self.dummy.prev
        tail.next = cur
        cur.prev = tail
        cur.next = self.dummy
        self.dummy.prev = cur
        heapq.heappush(self.heap, -x)
        self.val_to_node[x].append(cur)

    def pop(self) -> int:
        cur = self.popNode()
        return cur.val
    
    def popNode(self, node=None):
        if not node:
            node = self.dummy.prev
        
        prev_node, next_node = node.prev, node.next
        prev_node.next, next_node.prev = next_node, prev_node
        self.val_to_node[node.val].pop()
        
        return node

    def top(self) -> int:
        return self.dummy.prev.val

    def peekMax(self) -> int:
        while not self.val_to_node[-self.heap[0]]:
            heapq.heappop(self.heap)
        
        return -self.heap[0]

    def popMax(self) -> int:
        while not self.val_to_node[-self.heap[0]]:
            heapq.heappop(self.heap)
        
        max_val = -self.heap[0]
        node = self.val_to_node[max_val][-1]
        self.popNode(node)
        return max_val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()