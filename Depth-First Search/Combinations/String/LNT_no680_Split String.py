from typing import (
    List,
)

class Solution:
    """
    @param s: a string to be split
    @return: all possible split string array
    """
    def split_string(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, 0, [], res)
        return res

    def dfs(self, s, start, temp, res):
        if start == len(s):
            res.append(temp[:])
            return

        for i in range(start, start + 2):
            if i + 1 <= len(s):
                temp.append(s[start:i+1])
                self.dfs(s, i + 1, temp, res)
                temp.pop()