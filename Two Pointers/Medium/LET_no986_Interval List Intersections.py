class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        i = j = 0
        n1, n2 = len(firstList), len(secondList)
        while i < n1 and j < n2:
            f1, f2 = firstList[i]
            s1, s2 = secondList[j]
            if f1 <= s2 and s1 <= f2:
                res.append([max(f1, s1), min(f2, s2)])
            if f2 <= s2:
                i += 1
            else:
                j += 1
            
        return res