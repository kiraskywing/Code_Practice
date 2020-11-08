class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        if len(arr) < 3:
            return arr

        length = len(arr)
        judge = 0

        while judge < length - 2:
            pre_left = arr[0]
            judge = 0

            for i in range(1, length - 1):

                if arr[i] > pre_left and arr[i] > arr[i + 1]:
                    pre_left = arr[i]
                    arr[i] -= 1
                elif arr[i] < pre_left and arr[i] < arr[i + 1]:
                    pre_left = arr[i]
                    arr[i] += 1
                else:
                    pre_left = arr[i]
                    judge += 1

        return arr