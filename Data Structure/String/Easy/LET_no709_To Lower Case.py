class Solution:
    def toLowerCase(self, s: str) -> str:
        return ''.join(chr(ord(c) - ord('A') + ord('a')) if 'A' <= c <= 'Z' else c for c in s)