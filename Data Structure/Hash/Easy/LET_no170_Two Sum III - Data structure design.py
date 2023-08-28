class TwoSum:

    def __init__(self):
        self.memo = collections.defaultdict(int)

    def add(self, number: int) -> None:
        self.memo[number] += 1

    def find(self, value: int) -> bool:
        for key in self.memo:
            if value - key in self.memo and (value - key != key or self.memo[value - key] > 1):
                return True
        
        return False



# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)