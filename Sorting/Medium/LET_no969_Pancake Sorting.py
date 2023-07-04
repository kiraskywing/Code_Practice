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

class Solution2:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
        for i in range(n - 1, 0, -1):
            max_i = 0
            for j in range(1, i + 1):
                if arr[j] > arr[max_i]:
                    max_i = j
            if max_i != 0 and max_i != i:
                res.extend([max_i + 1, i + 1])
                arr[:max_i+1] = reversed(arr[:max_i+1])
                arr[:i+1] = reversed(arr[:i+1])
            elif max_i == 0:
                res.append(i + 1)
                arr[:i+1]= reversed(arr[:i+1])
        
        return res