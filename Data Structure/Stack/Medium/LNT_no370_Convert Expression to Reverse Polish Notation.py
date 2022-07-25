from typing import (
    List,
)

class Solution:
    """
    @param expression: A string array
    @return: The Reverse Polish notation of this expression
    """
    def convert_to_r_p_n(self, expression: List[str]) -> List[str]:
        res = []
        temp = []
        for s in expression:
            if s[0].isdigit():
                res.append(s)
            elif s == '(':
                temp.append(s)
            elif s == ')':
                while temp[-1] != '(':
                    res.append(temp.pop())
                temp.pop()
            else:
                rank = self.getRank(s)
                while temp and self.getRank(temp[-1]) >= rank:
                    res.append(temp.pop())
                temp.append(s)
        
        while temp:
            res.append(temp.pop())
        return res

    def getRank(self, c):
        if c in "*/":
            return 2
        elif c in "+-":
            return 1
        return 0
