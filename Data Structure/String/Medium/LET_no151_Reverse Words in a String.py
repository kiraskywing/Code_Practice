class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        temp = s.split()
        return ' '.join(reversed(temp))
