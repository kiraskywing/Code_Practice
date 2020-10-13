class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        self.id = [i for i in range(n)]
        self.count = n

        for i, j in connections:
            self.union(i, j)

        if self.count <= 1:
            return 0
        return self.count - 1

    def union(self, i, j):
        i2, j2 = self.find(i), self.find(j)
        if i2 == j2:
            return
        self.id[i2] = j2
        self.count -= 1

    def find(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i