from typing import (
    List,
)

class Solution:
    """
    @param logs: the logs
    @return: the logs after sorting
    """
    def log_sort(self, logs: List[str]) -> List[str]:
        memo_str = []
        memo_num = []
        for s in logs:
            key, content = s.split(' ', 1)
            if content[0].isdigit():
                memo_num.append(s)
            else:
                memo_str.append((key, content))
        memo_str.sort(key=lambda x : (x[1], x[0]))
        res = []
        for key, content in memo_str:
            res.append(key + " " + content)
        res += memo_num

        return res
