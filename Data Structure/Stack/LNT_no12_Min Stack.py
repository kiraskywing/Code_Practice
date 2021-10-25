# The same as LeetCode no155. Min Stack

class MinStack:

    def __init__(self):

        self.main = []
        self.sub = []

    """
    @param: number: An integer
    @return: nothing
    """

    def push(self, number):

        self.main.append(number)

        if not self.sub or number <= self.sub[-1]:
            self.sub.append(number)

    """
    @return: An integer
    """

    def pop(self):

        val = self.main.pop()

        if val == self.sub[-1]:
            self.sub.pop()

        return val

    """
    @return: An integer
    """

    def min(self):
        return self.sub[-1]