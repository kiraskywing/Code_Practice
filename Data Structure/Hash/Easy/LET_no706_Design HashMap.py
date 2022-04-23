class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 777
        self.buckets = [None] * self.size

    def put(self, key: int, value: int) -> None:
        idx = key % self.size
        cur = self.buckets[idx]
        if not cur:
            self.buckets[idx] = Node(key, value)
            return
        
        if cur.key == key:
            cur.val = value
        else:
            while cur.next:
                if cur.next.key == key:
                    cur.next.val = value
                    return
                cur = cur.next
            cur.next = Node(key, value)

    def get(self, key: int) -> int:
        idx = key % self.size
        cur = self.buckets[idx]
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        idx = key % self.size
        cur = self.buckets[idx]
        if not cur:
            return
        
        if cur.key == key:
            self.buckets[idx] = cur.next
        else:
            while cur.next:
                if cur.next.key == key:
                    cur.next = cur.next.next
                    return
                cur = cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)