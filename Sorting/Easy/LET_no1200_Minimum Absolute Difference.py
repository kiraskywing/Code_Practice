class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = [[arr[0], arr[1]]]
        diff = arr[1] - arr[0]
        
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] == diff:
                res.append([arr[i - 1], arr[i]])
            elif arr[i] - arr[i - 1] < diff:
                diff = arr[i] - arr[i - 1]
                res = [[arr[i - 1], arr[i]]]
        
        return res