class FreqStack:

    def __init__(self):
        self.max_freq = 0
        self.stack = collections.defaultdict(list)
        self.val_count = collections.defaultdict(int)

    def push(self, val: int) -> None:
        self.val_count[val] += 1
        self.max_freq = max(self.max_freq, self.val_count[val])
        self.stack[self.val_count[val]].append(val)

    def pop(self) -> int:
        res = self.stack[self.max_freq].pop()
        if not self.stack[self.max_freq]:
            self.max_freq -= 1
        self.val_count[res] -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()