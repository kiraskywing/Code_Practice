class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """

    def intersectionOfArrays(self, arrs):
        counter = collections.defaultdict(int)
        for arr in arrs:
            for i in arr:
                counter[i] += 1

        result = 0
        for num in counter:
            if counter[num] == len(arrs):
                result += 1
        return result
