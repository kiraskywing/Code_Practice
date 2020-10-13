class Solution:
    """
    @param s: a string
    @return: reverse only the vowels of a string
    """

    def reverseVowels(self, s):
        memo = {'a', 'e', 'i', 'o', 'u', "A", "E", "I", "O", "U"}
        string = [ch for ch in s]
        left, right = 0, len(string) - 1

        while left <= right:
            while left <= right and string[left] not in memo:
                left += 1
            while left <= right and string[right] not in memo:
                right -= 1
            if left <= right:
                string[left], string[right] = string[right], string[left]
                left += 1
                right -= 1

        return ''.join(string)
