class ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """
    def __init__(self, v1, v2):
        self.v1, self.v2 = v1, v2
        self.i, self.j = 0, 0
        self.alter = 0

    """
    @return: An integer
    """
    def next(self):
        self.alter += 1
        if self.alter % 2 != 0 and self.i < len(self.v1) or self.j >= len(self.v2):
            self.i += 1
            return self.v1[self.i - 1]
        if self.alter % 2 == 0 and self.j < len(self.v2) or self.i >= len(self.v1):
            self.j += 1
            return self.v2[self.j - 1]

    """
    @return: True if has next
    """
    def hasNext(self):
        return self.i < len(self.v1) or self.j < len(self.v2)


# Your ZigzagIterator object will be instantiated and called as such:
# solution, result = ZigzagIterator(v1, v2), []
# while solution.hasNext(): result.append(solution.next())
# Output result