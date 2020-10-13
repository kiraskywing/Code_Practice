class Solution:
    """
    @param s: a string
    @return: return a string
    """

    def removeDuplicateLetters(self, s):

        rec = {}
        for char in s:
            if char not in rec:
                rec[char] = 1
            else:
                rec[char] += 1

        visit = {}
        for char in rec:
            visit[char] = False

        res = []

        for char in s:
            rec[char] -= 1

            if visit[char]:
                continue

            while len(res) > 0 and res[-1] > char and rec[res[-1]] > 0:
                visit[res[-1]] = False
                res.pop()

            res.append(char)
            visit[char] = True

        return "".join(res)