class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        return ' '.join(reversed(s.split()))
        
        """
        r = s.split()
        p = ''

        if not r:
            return p

        else:
            for i in range(len(r)):
                p += r[len(r) - 1 - i] + ' '

            return p[0:-1]
        """
