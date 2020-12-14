class Solution:
    """
    @param s: a string
    @return: return a string
    """

    def removeDuplicateLetters(self, s):
        rec = collections.defaultdict(int)
        for ch in s:
            rec[ch] += 1

        visit = dict()
        for ch in rec:
            visit[ch] = False

        res = []

        for ch in s:
            rec[ch] -= 1

            if visit[ch]:
                continue

            while len(res) > 0 and res[-1] > ch and rec[res[-1]] > 0:
                visit[res[-1]] = False
                res.pop()

            res.append(ch)
            visit[ch] = True

        return "".join(res)