class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """

    def strStr(self, source, target):
        if len(source) < len(target):
            return -1

        len_s, len_t = len(source), len(target)
        for i in range(len_s - len_t + 1):
            if self.same_string(source[i: i + len_t], target):
                return i
        return -1

    def same_string(self, s1, s2):
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return False
        return True