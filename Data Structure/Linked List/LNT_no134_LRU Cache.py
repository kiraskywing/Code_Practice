class LinkedNode:

    def __init__(self, key=None, value=None):
        self.key = key
        self.val = value
        self.next = next


class LRUCache:
    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        self.key_to_prev = {}
        self.dummy = LinkedNode()
        self.tail = self.dummy
        self.capacity = capacity

    """
    @param: key: An integer
    @return: An integer
    """

    def get(self, key):
        if key not in self.key_to_prev:
            return -1
        self.kick(self.key_to_prev[key])
        return self.key_to_prev[key].next.val

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """

    def set(self, key, value):
        if key in self.key_to_prev:
            self.kick(self.key_to_prev[key])
            self.key_to_prev[key].next.val = value
            return

        self.push_to_tail(LinkedNode(key, value))
        if len(self.key_to_prev) > self.capacity:
            self.pop_front()

    """
    Methods are below.
    """

    def kick(self, prev):
        node = prev.next

        if node == self.tail:
            return

        prev.next = prev.next.next
        self.key_to_prev[node.next.key] = prev
        node.next = None
        self.push_to_tail(node)

    def push_to_tail(self, node):
        self.key_to_prev[node.key] = self.tail
        self.tail.next = node
        self.tail = node

    def pop_front(self):
        head = self.dummy.next
        del self.key_to_prev[head.key]
        self.dummy.next = self.dummy.next.next
        self.key_to_prev[head.next.key] = self.dummy
