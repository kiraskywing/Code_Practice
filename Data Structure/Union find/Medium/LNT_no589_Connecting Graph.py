class ConnectingGraph:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def connect(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa != pb:
            self.parent[pb] = pa

    """
    @param: a: An integer
    @param: b: An integer
    @return: A boolean
    """
    def query(self, a, b):
        return self.find(a) == self.find(b)
