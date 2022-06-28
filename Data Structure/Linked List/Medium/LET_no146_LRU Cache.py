class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = Node(-1, -1)
        self.tail = self.dummy
        self.memo = dict()

    def get(self, key: int) -> int:
        if key not in self.memo:
            return -1
        cur = self.memo[key]
        self.kickToTail(cur)
        return cur.val

    def put(self, key: int, value: int) -> None:
        if key in self.memo:
            cur = self.memo[key]
            cur.val = value
            self.kickToTail(cur)
        else:
            cur = Node(key, value)
            self.memo[key] = cur
            self.addToTail(cur)
            if self.capacity == 0:
                self.popFront()
            else:
                self.capacity -= 1
                
    
    def popFront(self) -> None:
        pop_node = self.dummy.next
        self.connectPrevNext(pop_node)
        del self.memo[pop_node.key]
    
    def connectPrevNext(self, cur: Node) -> None:
        prev_node = cur.prev
        next_node = cur.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def addToTail(self, node: Node) -> None:
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        
    def kickToTail(self, node: Node) -> None:
        if node is self.tail:
            return
        self.connectPrevNext(node)
        self.addToTail(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)