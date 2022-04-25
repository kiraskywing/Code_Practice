class ZigzagIterator2:
    """
    @param: vecs: a list of 1d vectors
    """
    def __init__(self, vecs):
        self.queue = collections.deque([(0, v) for v in vecs if v])

    """
    @return: An integer
    """
    def _next(self):
        i, arr = self.queue.popleft()
        res = arr[i]
        i += 1
        if i < len(arr):
            self.queue.append((i, arr))
        return res

    """
    @return: True if has next
    """
    def hasNext(self):
        return len(self.queue) > 0

# Your ZigzagIterator2 object will be instantiated and called as such:
# solution, result = ZigzagIterator2(vecs), []
# while solution.hasNext(): result.append(solution.next())
# Output result