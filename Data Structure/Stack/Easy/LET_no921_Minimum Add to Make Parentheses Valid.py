class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left = right = 0
        for c in s:
            if c == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
            else:
                left += 1
        
        return left + right