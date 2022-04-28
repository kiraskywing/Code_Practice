class Solution:
    """
    @param s: the string that represents a number
    @return: whether the string is a valid number
    """
    def is_number(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left <= right and s[left] == ' ':
            left += 1
        while left <= right and s[right] == ' ':
            right -= 1
        
        if left > right:
            return False
        if s[left] in "+-":
            left += 1
        if left > right:
            return False

        d, e = -1, -1
        for i in range(left, right + 1):
            if s[i] in "0123456789":
                continue
            if s[i] == '.':
                if d >= 0:
                    return False
                else:
                    d = i
            elif s[i] in "eE":
                if e >= 0:
                    return False
                else:
                    e = i
            else:
                return False
        
        if e == left or e == right:
            return False
        if d == left:
            return d < right and s[d + 1] in "0123456789"
        if d == right:
            return d > left and s[d - 1] in "0123456789"
        return True
