# the same as LeetCode no151. Reverse Words in a String

class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        temp = [string for string in s.split() if string]
        return ' '.join(temp[::-1])
