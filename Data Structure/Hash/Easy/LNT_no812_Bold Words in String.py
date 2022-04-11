from typing import (
    List,
)

class Solution:
    """
    @param words: the words
    @param s: the string
    @return: the string with least number of tags
    """
    def bold_words(self, words: List[str], s: str) -> str:
        bold = set()
        for w in words:
            i = s.find(w, 0)
            while i >= 0:
                bold.update(range(i, i + len(w)))
                i = s.find(w, i + 1)
        
        res = []
        for i in range(len(s)):
            if i in bold and i - 1 not in bold:
                res.append("<b>")
            res.append(s[i])
            if i in bold and i + 1 not in bold:
                res.append("</b>")
        return ''.join(res)
