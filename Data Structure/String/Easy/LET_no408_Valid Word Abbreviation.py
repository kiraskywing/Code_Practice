class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        num = 0
        for c in abbr:
            if c.isdigit():
                if num == 0 and c == '0':
                    return False
                num = num * 10 + int(c)
            else:
                i += num
                if i == len(word) or word[i] != c:
                    return False
                i += 1
                num = 0
            
        return i + num == len(word)