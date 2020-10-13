import random


class RandomizedSet:

    def __init__(self):
        self.pos = {}
        self.nums = []

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """

    def insert(self, val):
        if val in self.pos:
            return False

        self.nums.append(val)
        self.pos[val] = len(self.nums) - 1
        return True

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """

    def remove(self, val):
        if val not in self.pos:
            return False

        index = self.pos[val]
        self.nums[index], self.nums[-1] = self.nums[-1], self.nums[index]
        self.pos[self.nums[index]] = index
        del self.pos[val]
        self.nums.pop()
        return True

    """
    @return: Get a random element from the set
    """

    def getRandom(self):
        index = random.randint(0, len(self.nums) - 1)
        return self.nums[index]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()