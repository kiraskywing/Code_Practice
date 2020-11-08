class Solution:
    """
    @param s: A string
    @return: An integer
    """

    def atoi(self, s):

        if not s:
            return 0

        s = s.strip()
        neg, result = 1, 0

        for index in range(len(s)):

            if index == 0:
                if s[index] == "-":
                    neg = -1
                    continue
                if s[index] == "+":
                    neg = 1
                    continue

            if ord(s[index]) >= ord("0") and ord(s[index]) <= ord("9"):
                result = result * 10 + int(s[index])
            else:
                break

            index += 1

        result *= neg
        val_max, val_min = 2 ** 31 - 1, -(2 ** 31)

        if result > val_max:
            return val_max
        elif result < val_min:
            return val_min
        else:
            return result