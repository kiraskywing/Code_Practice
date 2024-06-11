class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        memo = {num : i for i, num in enumerate(arr2)}
        arr1.sort(key=lambda x: memo.get(x, x + 1000))
        return arr1