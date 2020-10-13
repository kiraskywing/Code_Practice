"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""


class NestedIterator(object):

    def __init__(self, nestedList):
        self.next_elem = None
        self.stack = []
        for item in reversed(nestedList):
            self.stack.append(item)

    # @return {int} the next element in the iteration
    def next(self):
        temp, self.next_elem = self.next_elem, None
        return temp

    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        while self.stack:
            item = self.stack.pop()
            if item.isInteger():
                self.next_elem = item.getInteger()
                return True
            for next_item in reversed(item.getList()):
                self.stack.append(next_item)

        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())