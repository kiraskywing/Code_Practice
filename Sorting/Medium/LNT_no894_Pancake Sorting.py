class Solution:
    """
    @param array: an integer array
    @return: nothing
    """

    def pancakeSort(self, array):
        n = len(array)

        for i in range(n - 1, 0, -1):
            Max = 0
            for j in range(1, i + 1):
                if array[j] > array[Max]:
                    Max = j
            if Max != 0 and Max != i:
                FlipTool.flip(array, Max)
                FlipTool.flip(array, i)

            if Max == 0:
                FlipTool.flip(array, i)
