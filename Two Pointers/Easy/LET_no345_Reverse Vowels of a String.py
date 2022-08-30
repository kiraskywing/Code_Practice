class Solution:
    def reverseVowels(self, s: str) -> str:
        # string size ? => at least single char
        # chars in the string? all printable chars
        # Both uppercase and lowercase? => yes
        
        # use two pointers start from the leftmost and the rightmost, 
        # and then move toward each other.
        # pointers stop when meet ['a', 'e', 'i', 'o', 'u'] => swap
        
        # immutable string in Python, convert string to chars array 
        # Time: O(n), Space: O(n)
        s = list(s) 
        
        left, right = 0, len(s) - 1
        while left < right:    # Time: O(n)
            while left < right and s[left].lower() not in "aeiou":
                left += 1
            while left < right and s[right].lower() not in "aeiou":
                right -= 1
            if left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        
        return ''.join(s)    # contruct string, Time: O(n)