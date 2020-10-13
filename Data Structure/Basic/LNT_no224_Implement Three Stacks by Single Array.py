class ThreeStacks:
    """
    @param: size: An integer
    """

    def __init__(self, size):
        self.stack = [None for _ in range(size * 3)]
        self.size = size
        self.p1, self.p2, self.p3 = 0, self.size, self.size * 2

    """
    @param: stackNum: An integer
    @param: value: An integer
    @return: nothing
    """

    def push(self, stackNum, value):
        if stackNum == 0:
            self.stack[self.p1] = value
            self.p1 += 1
        if stackNum == 1:
            self.stack[self.p2] = value
            self.p2 += 1
        if stackNum == 2:
            self.stack[self.p3] = value
            self.p3 += 1

    """
    @param: stackNum: An integer
    @return: the top element
    """

    def pop(self, stackNum):
        if stackNum == 0:
            self.p1 -= 1
            val = self.stack[self.p1]
        if stackNum == 1:
            self.p2 -= 1
            val = self.stack[self.p2]
        if stackNum == 2:
            self.p3 -= 1
            val = self.stack[self.p3]
        return val

    """
    @param: stackNum: An integer
    @return: the top element
    """

    def peek(self, stackNum):
        if stackNum == 0:
            val = self.stack[self.p1 - 1]
        if stackNum == 1:
            val = self.stack[self.p2 - 1]
        if stackNum == 2:
            val = self.stack[self.p3 - 1]
        return val

    """
    @param: stackNum: An integer
    @return: true if the stack is empty else false
    """

    def isEmpty(self, stackNum):
        if stackNum == 0:
            return self.p1 == 0
        if stackNum == 1:
            return self.p2 == self.size
        if stackNum == 2:
            return self.p3 == self.size * 2
