class Solution(object):

    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        stack = [nestedList]
        res = []
        while stack:
            cur = stack.pop()
            if isinstance(cur, list):
                for elem in reversed(cur):
                    stack.append(elem)
            else:
                res.append(cur)
        return res

class Solution2(object):

    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        res = []
        for val in nestedList:
            if type(val) is list:
                res.extend(self.flatten(val))
            else:
                res.append(val)
        
        return res