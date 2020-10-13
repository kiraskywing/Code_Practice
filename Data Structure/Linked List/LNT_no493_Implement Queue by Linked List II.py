class Dequeue:

    def __init__(self):
        self.head, self.tail = None, None

    """
    @param: item: An integer
    @return: nothing
    """
    def push_front(self, item):

        if not self.head:
            self.head = Node(item)
            self.tail = self.head
        else:
            tmp = Node(item)
            self.head.prev = tmp
            tmp.next = self.head
            self.head = tmp

    """
    @param: item: An integer
    @return: nothing
    """
    def push_back(self, item):

        if not self.tail:
            self.tail = Node(item)
            self.head = self.tail
        else:
            tmp = Node(item)
            self.tail.next = tmp
            tmp.prev = self.tail
            self.tail = tmp

    """
    @return: An integer
    """
    def pop_front(self):

        if self.head:
            res = self.head.val
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return res
        return False

    """
    @return: An integer
    """
    def pop_back(self):

        if self.tail:
            res = self.tail.val
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
            return res
        return False

class Node:

    def __init__(self, val):
        self.val = val
        self.prev, self.next = None, None