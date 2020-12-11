class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        i, j = 0, n - 1
        while i < n - 1 and arr[i + 1] > arr[i]:
            i += 1
        while j > 0 and arr[j - 1] > arr[j]:
            j -= 1
        
        return 0 < i == j < n - 1