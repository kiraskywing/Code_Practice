class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort(reverse=True)
        max_val = arr[0]

        while arr and target >= arr[-1] * len(arr):
            target -= arr.pop()

        if arr:
            if (target / len(arr)) % 1 > 0.5:
                return target // len(arr) + 1
            return target // len(arr)
        return max_val