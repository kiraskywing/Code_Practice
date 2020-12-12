class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        remove_L, remove_R = toBeRemoved[0], toBeRemoved[1]
        result = []

        for start, end in intervals:
            if start > remove_R or end < remove_L:
                result.append([start, end])
            else:
                if start < remove_L:
                    result.append([start, remove_L])
                if end > remove_R:
                    result.append([remove_R, end])

        return result