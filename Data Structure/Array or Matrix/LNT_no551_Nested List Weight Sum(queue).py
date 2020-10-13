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
from queue import Queue


class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):
        if not nestedList:
            return 0

        ans = 0
        queue = Queue()
        for item in nestedList:
            queue.put(item)
        depth = 0

        while not queue.empty():
            depth += 1
            length = queue.qsize()
            for i in range(length):
                item = queue.get()
                if item.isInteger():
                    ans += item.getInteger() * depth
                else:
                    for item2 in item.getList():
                        queue.put(item2)

        return ans
