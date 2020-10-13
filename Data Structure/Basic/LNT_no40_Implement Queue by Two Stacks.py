class MyQueue:

    def __init__(self):

        self.main = []
        self.sub = []

    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):

        self.main.append(element)

    """
    @return: An integer
    """
    def pop(self):

        while len(self.main) > 1:
            self.sub.append(self.main.pop())

        val = self.main.pop()

        while len(self.sub) > 0:
            self.main.append(self.sub.pop())

        return val

    """
    @return: An integer
    """
    def top(self):

        while len(self.main) > 0:
            self.sub.append(self.main.pop())

        val = self.sub[-1]

        while len(self.sub) > 0:
            self.main.append(self.sub.pop())

        return val