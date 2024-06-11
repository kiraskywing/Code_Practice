class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        i = j = 0
        m, n = len(firstList), len(secondList)

        while i < m and j < n:
            s1, e1 = firstList[i]
            s2, e2 = secondList[j]
            if s1 <= e2 and s2 <= e1:
                res.append([max(s1, s2), min(e2, e1)])
            if e1 <= e2:
                i += 1
            else:
                j += 1
        
        return res