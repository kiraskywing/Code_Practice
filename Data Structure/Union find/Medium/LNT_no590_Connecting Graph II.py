class ConnectingGraph2:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa != pb:
            self.parent[pb] = pa
            self.size[pa] += self.size[pb]

    """
    @param: a: An integer
    @return: An integer
    """
    def query(self, a):
        return self.size[self.find(a)]
