class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = []
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                result.append(chr(ord('a') + int(s[i:i+2]) - 1))
                i += 3
            else:
                result.append(chr(ord('a') + int(s[i]) - 1))
                i += 1
        return ''.join(result)