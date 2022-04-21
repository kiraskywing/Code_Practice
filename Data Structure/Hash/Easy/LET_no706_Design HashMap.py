# Similar with LeetCode no705. Design HashSet

class ListNode:
    def __init__(self, key, value):
        self.pair = [key, value]
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 1000
        self.h = [None] * self.m

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.m
        if not self.h[index]:
            self.h[index] = ListNode(key, value)
        else:
            cur = self.h[index]
            while True:
                if cur.pair[0] == key:
                    cur.pair[1] = value
                    return
                if not cur.next:
                    break
                cur = cur.next
            cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.m
        cur = self.h[index]
        while cur:
            if cur.pair[0] == key:
                return cur.pair[1]
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.m
        cur = self.h[index]
        if not cur:
            return
        if cur.pair[0] == key:
            self.h[index] = cur.next
        else:
            while cur.next:
                if cur.next.pair[0] == key:
                    cur.next = cur.next.next
                    return
                cur = cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)