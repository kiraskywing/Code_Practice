class MyQueue:

    def __init__(self):
        self.cur, self.head = None, None

    """
    @param: item: An integer
    @return: nothing
    """

    def enqueue(self, item):
        node = ListNode(item)
        if not self.head:
            self.cur = node
            self.head = self.cur
        else:
            self.cur.next = node
            self.cur = self.cur.next

    """
    @return: An integer
    """

    def dequeue(self):
        if self.head:
            val = self.head.val
            self.head = self.head.next
            return val
