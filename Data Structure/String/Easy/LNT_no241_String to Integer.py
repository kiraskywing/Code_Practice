class Solution:
    # @param {string} str a string
    # @return {int} an integer
    def stringToInteger(self, str):

        num, sig = 0, 1

        if str[0] == '-':
            sig = -1
            str = str[1:]

        for c in str:
            num = num * 10 + ord(c) - ord('0')

        return num * sig