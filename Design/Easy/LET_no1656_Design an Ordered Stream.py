class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 1
        self.arr = [None] * (n + 1)

    def insert(self, id: int, value: str) -> List[str]:
        self.arr[id] = value
        res = []
        if id == self.ptr:
            while self.ptr < len(self.arr) and self.arr[self.ptr]:
                res.append(self.arr[self.ptr])
                self.ptr += 1
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)