from random import randint


class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.indexs = collections.defaultdict(set)

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.nums.append(val)
        self.indexs[val].add(len(self.nums) - 1)
        return len(self.indexs[val]) == 1

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if not self.indexs[val]:
            return False
        x = self.indexs[val].pop()
        self.nums[x] = None
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        x = None
        while x is None:
            x = self.nums[randint(0, len(self.nums) - 1)]
        return x

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()