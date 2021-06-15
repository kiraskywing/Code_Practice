"""
In python, you can use list as stack
stack = [1,2,3,4]
Get top element: stack[-1]  -> 4
Pop element: stack.pop()   -> 4
Push element: stack.append(5)
check the size of stack: len(stack)
"""
class Solution:
    """
    @param: stk: an integer stack
    @return: void
    """
    def stackSorting(self, stk):

        temp = []

        while len(stk) > 0:
            top = stk.pop()
            while len(temp) > 0 and temp[-1] < top:
                stk.append(temp.pop())
            temp.append(top)

        while len(temp) > 0:
            stk.append(temp.pop())