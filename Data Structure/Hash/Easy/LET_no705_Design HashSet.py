class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.size = 777
        self.memo = [None] * self.size

    def add(self, key: int) -> None:
        idx = key % self.size
        cur = self.memo[idx]
        if not cur:
            self.memo[idx] = Node(key)
            return
        
        if cur.key == key:
            return
        else:
            while cur.next:
                if cur.next.key == key:
                    return
                cur = cur.next
            cur.next = Node(key)

    def remove(self, key: int) -> None:
        idx = key % self.size
        cur = self.memo[idx]
        if not cur:
            return
            
        if cur.key == key:
            self.memo[idx] = cur.next
        else:
            while cur.next:
                if cur.next.key == key:
                    cur.next = cur.next.next
                    return
                cur = cur.next

    def contains(self, key: int) -> bool:
        idx = key % self.size
        cur = self.memo[idx]
        while cur:
            if cur.key == key:
                return True
            cur = cur.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)