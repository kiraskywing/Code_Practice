class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """

    def expressionExpand(self, s):

        result = []
        for c in s:
            if c != "]":
                result.append(c)
                continue

            temp = []
            while result and result[-1] != "[":
                temp.append(result.pop())

            result.pop()

            repeat = 0
            base = 1
            while result and result[-1].isdigit():
                repeat += (ord(result.pop()) - ord("0")) * base
                base *= 10

            result.append(''.join(reversed(temp)) * repeat)

        return ''.join(result)
