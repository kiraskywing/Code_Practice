class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        s = list(s)
        pre = 0
        for i in range(len(shifts) - 1, -1, -1):
            cur = pre + shifts[i]
            pre = cur
            s[i] = chr(ord('a') + (ord(s[i]) - ord('a') + cur) % 26)
        return ''.join(s)