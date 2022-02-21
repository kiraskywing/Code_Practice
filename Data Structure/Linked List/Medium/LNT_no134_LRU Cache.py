# The same as LeetCode no146. LRU Cache

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = Node(-1, -1)
        self.tail = self.dummy
        self.memo = {}

    def get(self, key: int) -> int:
        if key not in self.memo:
            return -1
        cur = self.memo[key]
        self.kick(cur)
        return cur.val

    def put(self, key: int, value: int) -> None:
        if key in self.memo:
            cur = self.memo[key]
            self.kick(cur)
            cur.val = value
            return
        
        cur = Node(key, value)
        self.memo[key] = cur
        self.pushToTail(cur)
        if len(self.memo) > self.capacity:
            self.popFront()
    
    def kick(self, cur):
        if cur is self.tail:
            return
        p, n = cur.prev, cur.next
        p.next = n
        n.prev = p
        self.pushToTail(cur)
    
    def pushToTail(self, cur):
        self.tail.next = cur
        cur.prev = self.tail
        cur.next = None
        self.tail = cur
    
    def popFront(self):
        head = self.dummy.next
        nxt = head.next
        del self.memo[head.key]
        self.dummy.next = nxt
        nxt.prev = self.dummy


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)