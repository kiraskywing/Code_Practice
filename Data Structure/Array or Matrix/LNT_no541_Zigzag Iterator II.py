class ZigzagIterator2:
    """
    @param: vecs: a list of 1d vectors
    """
    def __init__(self, vecs):
        self.lst = [collections.deque(v) for v in vecs]
        self.i = 0

    """
    @return: An integer
    """
    def next(self):
        val = self.lst[self.i].popleft()
        self.i = (self.i + 1) % len(self.lst)
        return val

    """
    @return: True if has next
    """
    def hasNext(self):
        for _ in range(len(self.lst)):
            if self.lst[self.i]:
                return True
            self.i = (self.i + 1) % len(self.lst)
        return False

# Your ZigzagIterator2 object will be instantiated and called as such:
# solution, result = ZigzagIterator2(vecs), []
# while solution.hasNext(): result.append(solution.next())
# Output result