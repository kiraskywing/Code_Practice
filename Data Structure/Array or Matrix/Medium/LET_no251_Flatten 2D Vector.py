class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.i, self.j = 0, 0
        self.vec = vec

    def next(self) -> int:
        self.hasNext()
        self.j += 1
        return self.vec[self.i][self.j - 1]

    def hasNext(self) -> bool:
        while self.i < len(self.vec) and self.j == len(self.vec[self.i]):
            self.i += 1
            self.j = 0
        return self.i < len(self.vec)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()