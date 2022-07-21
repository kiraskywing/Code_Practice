class ConnectingGraph3:
    """
    @param a: An integer
    @param b: An integer
    @return: nothing
    """
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.size = n
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def find(self, i):
        res = i
        while self.parent[res] != res:
            res = self.parent[res]
        while self.parent[i] != res:
            i2 = self.parent[i]
            self.parent[i] = res
            i = i2
        return res
    
    def connect(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa != pb:
            self.parent[pb] = pa
            self.size -= 1

    """
    @return: An integer
    """
    def query(self):
        return self.size