class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = count = 0;
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                count = count + 1 if count > 0 else 1
            elif arr[i] < arr[i + 1]:
                count = count - 1 if count < 0 else -1
            else:
                count = 0
            res = max(res, abs(count))
            count *= -1
        return res + 1