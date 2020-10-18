class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        return sum(arr[len(arr) // 20 : -len(arr) // 20]) / (len(arr) * 9 // 10)