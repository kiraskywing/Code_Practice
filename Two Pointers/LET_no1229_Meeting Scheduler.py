class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:

        if not slots1 or not slots2 or duration is None:
            return []

        i, j, len_1, len_2 = 0, 0, len(slots1), len(slots2)

        slots1.sort()
        slots2.sort()

        while i < len_1 and j < len_2:

            while i < len_1 and j < len_2 and (slots1[i][1] - slots1[i][0] < duration or slots1[i][1] <= slots2[j][0]):
                i += 1
            while i < len_1 and j < len_2 and (slots2[j][1] - slots2[j][0] < duration or slots2[j][1] <= slots1[i][0]):
                j += 1

            if i < len_1 and j < len_2 and min(slots1[i][1], slots2[j][1]) - max(slots1[i][0], slots2[j][0]) >= duration:
                return [max(slots1[i][0], slots2[j][0]), max(slots1[i][0], slots2[j][0]) + duration]

            i += 1
            j += 1

        return []