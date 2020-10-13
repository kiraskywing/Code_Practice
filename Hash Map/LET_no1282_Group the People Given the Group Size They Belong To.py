class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        result = []
        memo = {}
        for i, g_size in enumerate(groupSizes):
            if g_size not in memo:
                memo[g_size] = [i]
            else:
                memo[g_size].append(i)

        for g_size in memo:
            temp = []
            for i in memo[g_size]:
                temp.append(i)
                if len(temp) == g_size:
                    result.append(temp)
                    temp = []

        return result
